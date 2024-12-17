import Cookies from 'js-cookie';

export const getAuthHeaders = () => {
    const jwtToken = Cookies.get('jwtToken');
    let headers: Record<string, string> = {};
    if (jwtToken) {
        headers['Authorization'] = `Bearer ${jwtToken}`;
    }
    return headers;
}