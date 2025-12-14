# Database model definitions

from datetime import datetime
from typing import Optional
from enum import Enum


class KeywordType(str, Enum):
    GOLDEN = "golden"
    NORMAL = "normal"
    RELATED = "related"


class PostStatus(str, Enum):
    DRAFT = "draft"
    REVIEWED = "reviewed"
    PUBLISHED = "published"


class Subject:
    """주제 모델"""
    
    def __init__(
        self,
        id: str,
        name: str,
        description: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at


class Keyword:
    """키워드 모델"""
    
    def __init__(
        self,
        id: str,
        name: str,
        type: KeywordType,
        description: Optional[str] = None,
        search_volume: int = 0,
        view_count: int = 0,
        document_count: int = 0,
        is_golden: bool = False,
        subject_id: Optional[str] = None,
        related_keyword_id: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.search_volume = search_volume
        self.view_count = view_count
        self.document_count = document_count
        self.is_golden = is_golden
        self.subject_id = subject_id
        self.related_keyword_id = related_keyword_id
        self.created_at = created_at
        self.updated_at = updated_at


class User:
    """사용자 모델"""
    
    def __init__(
        self,
        id: str,
        username: str,
        email: str,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.id = id
        self.username = username
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at


class BlogAccount:
    """블로그 계정 모델"""
    
    def __init__(
        self,
        id: str,
        user_id: str,
        blog_id: str,
        login_status: bool = False,
        session_data: Optional[str] = None,
        last_login_at: Optional[datetime] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.id = id
        self.user_id = user_id
        self.blog_id = blog_id
        self.login_status = login_status
        self.session_data = session_data
        self.last_login_at = last_login_at
        self.created_at = created_at
        self.updated_at = updated_at


class Image:
    """이미지 모델"""
    
    def __init__(
        self,
        id: str,
        url: str,
        filename: Optional[str] = None,
        file_size: Optional[int] = None,
        mime_type: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.id = id
        self.url = url
        self.filename = filename
        self.file_size = file_size
        self.mime_type = mime_type
        self.created_at = created_at
        self.updated_at = updated_at


class Post:
    """포스팅 모델"""
    
    def __init__(
        self,
        id: str,
        title: str,
        content: str,
        keyword_id: Optional[str] = None,
        status: PostStatus = PostStatus.DRAFT,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.id = id
        self.title = title
        self.content = content
        self.keyword_id = keyword_id
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at


class PostImage:
    """포스팅-이미지 중간 테이블 모델"""
    
    def __init__(
        self,
        post_id: str,
        image_id: str,
        display_order: int = 0,
        created_at: Optional[datetime] = None
    ):
        self.post_id = post_id
        self.image_id = image_id
        self.display_order = display_order
        self.created_at = created_at
