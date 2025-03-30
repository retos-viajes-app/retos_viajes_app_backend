from datetime import datetime
from fastapi import APIRouter, HTTPException, FastAPI, Depends, Query
from sqlalchemy import case
from sqlalchemy.orm import Session, joinedload
from app.auth.auth import  get_current_user, verify_access_token
from app.db.model.user import User
from app.db.db_connection import get_db
from app.db.model.user_connection import UserConnection
from app.schema.user_connection import UserConnectionRequest,  UserConnectionResponse
from app.db.model.completed_challenge import CompletedChallenge
from app.db.model.challenge import Challenge

from app.schema.pagination_info import PaginationInfo
from app.schema.completed_challenge import CompletedChallengeResponse, CompletedChallengesSuggestedResponse
from app.schema.user import UserResponse
from app.schema.category import CategoryResponse
from app.schema.destination import DestinationResponse
from app.schema.challenge import ChallengeResponse

router = APIRouter(tags=["completed_challenges"])

#Endpoint para obtener completed challenges sugeridos de otros usuarios que tengan conexión contigo
@router.get("/completed_challenges/suggested", response_model=CompletedChallengesSuggestedResponse)
def get_suggested_completed_challenges(
    page: int = Query(1, alias="page", ge=1),
    per_page: int = Query(10, alias="per_page", le=50),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)):

    # Subconsulta para obtener los IDs de los usuarios conectados
    subquery = db.query(
        case(
            (UserConnection.user_id_1 == current_user.id, UserConnection.user_id_2),
            else_=UserConnection.user_id_1
        )
    ).filter(
        (UserConnection.user_id_1 == current_user.id) | (UserConnection.user_id_2 == current_user.id),
        UserConnection.status == "accepted"
    ).subquery()
    
    # Consulta principal con subconsulta para filtrar los completed challenges
    query = db.query(CompletedChallenge).join(Challenge).filter(
        CompletedChallenge.user_id.in_(db.query(subquery))
    ).options(
        joinedload(CompletedChallenge.user),
        joinedload(CompletedChallenge.challenge).joinedload(Challenge.category),
        joinedload(CompletedChallenge.challenge).joinedload(Challenge.destination)
    ).distinct().order_by(CompletedChallenge.completed_at.desc())
    
    offset = (page - 1) * per_page
    completed_challenges = query.offset(offset).limit(per_page + 1).all()
    has_more = len(completed_challenges) > per_page
    completed_challenges = completed_challenges[:per_page]

    completed_challenge_responses = [
        CompletedChallengeResponse(
            id=cc.id,
            user=UserResponse(
                id=cc.user.id,
                name=cc.user.name,
                email=cc.user.email,
                username=cc.user.username,
                profile_photo_url=cc.user.profile_photo_url
            ),
            challenge=ChallengeResponse(
                id=cc.challenge.id,
                title=cc.challenge.title,
                category=CategoryResponse(
                    id=cc.challenge.category.id,
                    name=cc.challenge.category.name,
                    icon_url=cc.challenge.category.icon_url
                ),
                destination=DestinationResponse(
                    id=cc.challenge.destination.id,
                    city=cc.challenge.destination.city,
                    country=cc.challenge.destination.country
                )
            ),
            completed_at=cc.completed_at,
            proof_photo_url=cc.proof_photo_url,
            description=cc.description,
        )
        for cc in completed_challenges
    ]


    return CompletedChallengesSuggestedResponse(
        completed_challenges=completed_challenge_responses,
        pagination=PaginationInfo(
            page=page,
            per_page=per_page,
            has_more=has_more
        )
    )
