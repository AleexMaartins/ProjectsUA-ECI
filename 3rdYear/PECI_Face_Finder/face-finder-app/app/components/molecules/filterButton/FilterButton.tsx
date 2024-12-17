import { IoFilter, IoFilterOutline } from "react-icons/io5";
import Button, { ButtonSize, ButtonVariant } from "../../atoms/button/Button";

export default function FilterButton()
{
    return (
        <div>
            <Button text="" 
                    size={ButtonSize.SMALL}  
                    variant={ButtonVariant.OUTLINED}
                    icon={
                        <IoFilterOutline/>
                    }
            />
        </div>
    );

}