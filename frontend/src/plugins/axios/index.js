import axios from "axios"
const  baseURL = "http://127.0.0.1:8000/",

    
instance = axios.create({
    baseURL: baseURL,
    headers: {
        'Content-Type': 'application/json',
    }
})


function clearStorage() {
    localStorage.removeItem("token")
    localStorage.removeItem("refresh_token")
    localStorage.removeItem("email")
    localStorage.removeItem("username")
}

instance.interceptors.request.use(config => {
    
    config.headers.Authorization = localStorage.getItem("token") ? `Bearer ${localStorage.getItem("token")}` : '';
    return config;
  }, error => {
    return Promise.reject(error);
  });


instance.interceptors.response.use(
 response => {
    return response
 },
 error => {
    const originalRequest = error.config;
    // Prevent infinite loops

    console.log(error);

    if (error.response.status === 401 && originalRequest.url === baseURL+'api/token/refresh/') {
        window.location.href = '/login/';
        return Promise.reject(error);
    }

    if (error.response.data.code === "token_not_valid" &&
        error.response.status === 401 && 
        error.response.statusText === "Unauthorized") 
        {
            const refreshToken = localStorage.getItem('refresh_token');
            if (refreshToken){
                const tokenParts = JSON.parse(atob(refreshToken.split('.')[1]));

                // exp date in token is expressed in seconds, while now() returns milliseconds:
                const now = Math.ceil(Date.now() / 1000);

                if (tokenParts.exp > now) {
                    return instance
                    .post('api/token/refresh/', {refresh: refreshToken})
                    .then((response) => {
        
                        localStorage.setItem('token', response.data.access);
                        // localStorage.setItem('refresh_token', response.data.refresh);
        
                        instance.defaults.headers['Authorization'] = "Bearer " + response.data.access;
                        originalRequest.headers['Authorization'] = "Bearer " + response.data.access;
        
                        return instance(originalRequest);
                    })
                    .catch(err => {
                        console.log(err)
                    });
                }else{
                    console.log("Refresh token is expired", tokenParts.exp, now);
                    clearStorage()
                    window.location.href = '/login/';
                }
            }else{
                console.log("Refresh token not available.")
                clearStorage()
                window.location.href = '/login/';
    }
    }
    
    
    // specific error handling done elsewhere
    return Promise.reject(error);
  }
);
export default instance