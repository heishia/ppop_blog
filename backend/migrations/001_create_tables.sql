-- Database schema migration
-- Create tables for PPOP Blog application

-- Create ENUM types
CREATE TYPE keyword_type AS ENUM ('golden', 'normal', 'related');
CREATE TYPE post_status AS ENUM ('draft', 'reviewed', 'published');

-- Create subjects table
CREATE TABLE subjects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_subjects_name ON subjects(name);

-- Create keywords table
CREATE TABLE keywords (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    type keyword_type NOT NULL DEFAULT 'normal',
    description TEXT,
    search_volume INTEGER DEFAULT 0,
    view_count INTEGER DEFAULT 0,
    document_count INTEGER DEFAULT 0,
    is_golden BOOLEAN DEFAULT FALSE,
    subject_id UUID REFERENCES subjects(id) ON DELETE SET NULL,
    related_keyword_id UUID REFERENCES keywords(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_keywords_name ON keywords(name);
CREATE INDEX idx_keywords_type ON keywords(type);
CREATE INDEX idx_keywords_subject_id ON keywords(subject_id);
CREATE INDEX idx_keywords_is_golden ON keywords(is_golden);
CREATE INDEX idx_keywords_search_volume ON keywords(search_volume);
CREATE INDEX idx_keywords_document_count ON keywords(document_count);

-- Create users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);

-- Create blog_accounts table
CREATE TABLE blog_accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE UNIQUE,
    blog_id VARCHAR(255) NOT NULL,
    login_status BOOLEAN DEFAULT FALSE,
    session_data TEXT,
    last_login_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_blog_accounts_user_id ON blog_accounts(user_id);
CREATE INDEX idx_blog_accounts_blog_id ON blog_accounts(blog_id);

-- Create images table
CREATE TABLE images (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    url TEXT NOT NULL,
    filename VARCHAR(255),
    file_size BIGINT,
    mime_type VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_images_url ON images(url);

-- Create posts table
CREATE TABLE posts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(500) NOT NULL,
    content TEXT NOT NULL,
    keyword_id UUID REFERENCES keywords(id) ON DELETE SET NULL,
    status post_status NOT NULL DEFAULT 'draft',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_posts_keyword_id ON posts(keyword_id);
CREATE INDEX idx_posts_status ON posts(status);
CREATE INDEX idx_posts_created_at ON posts(created_at DESC);

-- Create post_images junction table
CREATE TABLE post_images (
    post_id UUID REFERENCES posts(id) ON DELETE CASCADE,
    image_id UUID REFERENCES images(id) ON DELETE CASCADE,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    PRIMARY KEY (post_id, image_id)
);

CREATE INDEX idx_post_images_post_id ON post_images(post_id);
CREATE INDEX idx_post_images_image_id ON post_images(image_id);

-- Create function to update updated_at column
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create triggers for updated_at
CREATE TRIGGER update_subjects_updated_at BEFORE UPDATE ON subjects
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_keywords_updated_at BEFORE UPDATE ON keywords
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_blog_accounts_updated_at BEFORE UPDATE ON blog_accounts
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_images_updated_at BEFORE UPDATE ON images
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_posts_updated_at BEFORE UPDATE ON posts
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
