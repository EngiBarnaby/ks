import axios  from "@/plugins/axios"
import jwt_decode from "jwt-decode";
const userStore = {
    state: {
        username : "",
        email : "",
        usertToken : "",
        userRefreshtoken : "",
    },

    mutations: {
        
        getUserName(state){
            let token = localStorage.getItem("token")
            let decoded = jwt_decode(token)
            let username = decoded.user_name
            localStorage.setItem("username", username)
            state.username = username

            
        },

        initStore(state){
            if (localStorage.getItem("token") && localStorage.getItem("username") && localStorage.getItem("refresh_token")){
                state.username = localStorage.getItem("username")
                state.email = localStorage.getItem("email")
                state.usertToken = localStorage.getItem("token")
                state.userRefreshtoken = localStorage.getItem("refresh_token")
            }
            else {
                state.username = ""
                state.email = ""
                state.usertToken = ""
                state.userRefreshtoken = ""
            }
        }
    },

    actions: {
        loginUser(context, user){
            return new Promise((resolve, reject) => {
                axios({url : "api/token/", data : user, method : "POST"})
                .then( response  => {
                    const accessToken = response.data.access
                    const refreshToken = response.data.refresh
                    localStorage.setItem("token", accessToken)
                    localStorage.setItem("refresh_token", refreshToken)
                    localStorage.setItem("email", user.email)
                    axios.defaults.headers["Authorization"] = `Bearer ${accessToken}`
                    resolve(response)
                })
                .catch( error =>{
                    console.log(error);
                    localStorage.removeItem("token")
                    reject(error)
                })
            })
        }
    },

    getters: {
        getUserName : state => state.username
    }
}

export default userStore;