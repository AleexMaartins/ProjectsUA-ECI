import { IoMdArrowBack } from "react-icons/io"
import Button, { ButtonSize, ButtonVariant } from "../../atoms/button/Button"
import Text, { TextTypes } from "../../atoms/text/Text"
import standardHeaderSyle from './standardHeaderStyle.module.css'
import { ReactNode } from "react"

type StandardHeaderProps = {
    title:string
    arrowBack?:boolean,
    hasRigthButtons?: boolean
    mainButtonText?:string
    mainButtonIcon?: ReactNode
    secondaryButtonIcon?: ReactNode
    additionalButton?: ReactNode
    onClickArrowButton?: () => void;
    onClickMainButton?: () => void;
    onClickSecondaryButton?: () => void;
}
export default function StandardHeader({
    title, 
    arrowBack = false, 
    hasRigthButtons = true, 
    mainButtonText,
    mainButtonIcon,
    secondaryButtonIcon,
    additionalButton,
    onClickArrowButton,
    onClickMainButton,
    onClickSecondaryButton
}:StandardHeaderProps){

    return (
        <div className={standardHeaderSyle.headerContainer}>
            <div
                style={{display:"flex", alignItems:"center"}}
            >
                {
                    arrowBack &&
                        <IoMdArrowBack
                            cursor={"pointer"}
                            fontSize={"50px"}
                            color="#08263b"
                            onClick={onClickArrowButton ? onClickArrowButton : ()=>history.back()}
                        />
                }
                
                <div className={standardHeaderSyle.titleContainer}>
                    <Text
                        text={title} 
                        type={TextTypes.HEADER}
                        color="main-blue"
                    />
                </div>
            </div>
                {
                    hasRigthButtons && 
                    <div className={standardHeaderSyle.headerButtons}>
                        {mainButtonIcon && 
                            <Button 
                                size={ButtonSize.SMALL}  
                                variant={ButtonVariant.OUTLINED}
                                icon={mainButtonIcon}
                                onClick={onClickSecondaryButton}
                            />
                        }
                        {mainButtonText && 
                            <Button 
                                text={mainButtonText}
                                size={ButtonSize.BIG}
                                icon={secondaryButtonIcon}
                                onClick={onClickMainButton}
                            />
                        }
                        {additionalButton}
                    </div>
                }
        </div>
    )
}