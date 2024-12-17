
export enum ALBUM_VISIBILITY{
    PRIVATE = "Private", 
    PUBLIC= "Public"
}

export type Album = {
    id?: string
    god?: string
    title: string
    description?: string
    isPublic: boolean
    thumbnail?: string
    label?: string
    creationDate?: string
    ownerName?:string
}