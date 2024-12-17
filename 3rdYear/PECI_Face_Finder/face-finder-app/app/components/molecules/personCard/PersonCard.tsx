import Text, { TextTypes } from '../../atoms/text/Text'
import personCardStyle from './personCardStyle.module.css'

interface PersonCardProps {
    person: string;
    onClick:()=>void
    thumbnail: string;
}

export function PersonCard({ person, onClick, thumbnail }: PersonCardProps){
    return (
        <div 
            className={personCardStyle.card}
            onClick={onClick}
        >
                <div >
                    <img src={thumbnail} alt="" className={personCardStyle.personThumb}/>
                </div>
                <div className={personCardStyle.personName}>
                    <Text 
                        text={person} 
                        color="#08263b" 
                        fontSize='18px'
                    />
                </div>
        </div>
    )
}