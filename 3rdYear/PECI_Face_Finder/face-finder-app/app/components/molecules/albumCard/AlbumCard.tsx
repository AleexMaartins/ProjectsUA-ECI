import Text, { TextTypes } from '../../atoms/text/Text';
import { FaRegCalendar } from "react-icons/fa";
import { FaTag } from "react-icons/fa6";
import albumCardStyle from './albumCardStyle.module.css';
import { ALBUM_VISIBILITY } from '@/src/constants/album';

export type AlbumCardProps = {
    id:string
    title: string
    showLabel: boolean
    ownerName?:string
    label?:string
    thumbnail?:string
}
export default function AlbumCard({id, showLabel, title, ownerName, label,thumbnail  }: AlbumCardProps){
    return (
        <div className={albumCardStyle.cardContainer} onClick={() => window.location.assign(`albums/${id}`)}>
            <div className={albumCardStyle.albumThumb}>
                {thumbnail && <img src={thumbnail} alt="Album Thumbnail" style={{width: '100%', height: '100%', objectFit: 'cover'}} />} {/* Display the thumbnail if it exists */}
            </div>

            <div className={albumCardStyle.albumDescription}>
                <Text 
                    text={checkStringSize(title)} 
                    color="main-blue" 
                    fontSize='20px'
                />
                <Text 
                    text={checkStringSize(!showLabel ? `By ${ownerName}` : label ?? "") } 
                    color="main-blue" 
                    type={TextTypes.CAPTION} 
                />
            </div>
        </div>
    );
}

function checkStringSize(str: string): string {
    if (str.length >= 20) {
        return str.substring(0, 17) + "...";
    } else {
        return str;
    }
}