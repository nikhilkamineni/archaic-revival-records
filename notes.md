# Archaic Revival Records website


## Backend

### Models
- Artist
  - id: uuid
  - Name: char field
  - About: text field
  - Genre?: char field
  - Image?

- Release
  - id: UUID Field
  - Title: Char Field
  - Artist: ForeignKey field
  - About: Text field
  - Year: IntField
  - Link: url field
  - Album artwork: artwork link/image upload?
  - Tracklist: ?

- Track?
  - id: uuid
  - Title: char field
  - Album: uuid field
  - Link: url field


