from fastapi import Request, HTTPException
from starlette import status
from fastapi.responses import H


async def authenticate(request: Request, call_next):
    try:
        request.state.acack = request.cookies.get("acack")
        response = authentication_service.authenticate(request)
        return response
    except Exception as ext:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ext),
        ) from ext
