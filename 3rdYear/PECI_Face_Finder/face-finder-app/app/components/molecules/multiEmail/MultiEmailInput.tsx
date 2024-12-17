import { ReactMultiEmail } from "react-multi-email";
import Text from "../../atoms/text/Text";
import multiEmailStyle from './multiEmailStyle.module.css'
import { FaRegTrashAlt } from "react-icons/fa";
type MultiEmailInputProps = {
    emails: string[]
    onChange: (email:string[])=>void;
}
export default function MultiEmailInput({emails, onChange}:MultiEmailInputProps){
    return(
        <div className="hey">
            <ReactMultiEmail 
                emails={emails}
                onChange={(_emails: string[]) => onChange(_emails)}
                getLabel={(email, index, removeEmail) => {
                    return (
                        <div className="test">
                            <div data-tag key={index} >
                                <div data-tag-item className={multiEmailStyle.test}>
                                    {email}
                                    <span data-tag-handle className={multiEmailStyle.removeIcon} onClick={() => removeEmail(index)}>
                                        <FaRegTrashAlt />
                                    </span>
                                </div>
                            </div>
                        </div>
                        
                    );
                }}
            />
        </div>
       
    );
}