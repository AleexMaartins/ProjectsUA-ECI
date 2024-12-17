import React from 'react';
import css from './loading.module.css';
import loadWheel from '@/public/image/loading.gif';
import Image from 'next/image';

interface LoadingScreenProps {
    option?: 'option1' | 'option2';
}

const LoadingScreen: React.FC<LoadingScreenProps> = ({ option = 'option1' }) => {
    return (
        <div className={css.loadingContainer}>
            {option === 'option1' ? (
                <>
                    <Image src={loadWheel} alt="Loading" className={css.loadingImage} />
                    <h1 className={css.loadingText}>Loading...</h1>
                </>
            ) : (
                <h1 className={css.loadingTextB}>Loading...</h1>
            )}
        </div>
    );
};

export default LoadingScreen;