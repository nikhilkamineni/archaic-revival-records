# Archaic Revival Records website


## Backend

### Models
- Artist
  - id: uuid
  - Name: char field
  - About: text field
  - Releases: One-to-many field
  - Genre?: char field
  - Image?

- Release
  - id: uuid
  - Title: char field
  - Artist: uuid field
  - Description: text field
  - Link: url field
  - Album artwork: artwork link
  - Tracks?: uuid field

- Track?
  - id: uuid
  - Title: char field
  - Album: uuid field
  - Link: url field


