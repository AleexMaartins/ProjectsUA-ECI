import layoutStyle from './layoutStyle.module.css'
import logoB from '@/public/image/logoB.png'
import logo from '@/public/image/logo.png'
import NavBar from '../components/molecules/navBar/NavBar';


export default function AuthLayout({children}:{children:React.ReactNode}){
    return (
        <div className={layoutStyle.authContainer}>
            <div className={layoutStyle.imgContainer}></div>

            <div className={layoutStyle.contentContainer}>
                <NavBar noLinks/>
                {children}  
            </div>

        </div>
    );
}