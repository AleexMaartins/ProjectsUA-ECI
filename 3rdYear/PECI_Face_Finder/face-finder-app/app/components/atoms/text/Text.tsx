import textStyle from './textStyle.module.css'

export type TextProps = {
    text:string;
    type?: TextTypes;
    color?: string;
    fontSize?:string;
    link?: string
}

export enum TextTypes{
    HEADER,
    TEXT, 
    CAPTION, 
    SUBHEADER,
}

export default function Text({text, type, color, fontSize, link}:TextProps){
    const getTypeClass=()=>{
        switch (type) {
            case TextTypes.HEADER:
                return textStyle.header;
            case TextTypes.SUBHEADER:
                return textStyle.subHeader
            case TextTypes.CAPTION:
                return textStyle.caption;
            default:
                return textStyle.text;
        }
    }

    const textClasses =()=>{
        const typeClass = getTypeClass();

        return `${typeClass}`
    }
    const getColor = (color:string) =>{
        switch (color) {
            case 'main-red':
                return "#be3434"
            case 'main-blue':
                return "#08263b"
        
            default:
              return color
        }
    }
    return (
        <span 
            className={textClasses()} 
            style={{
                color: getColor(color?? ""),
                fontSize: fontSize
            }}
        >
            {
                link ? <a className={textStyle.linkStyle} href={link}>{text}</a> : text
            }

        </span>
    );
}