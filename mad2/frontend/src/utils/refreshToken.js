import axios from "axios"

async function refreshAccessToken(){

    let refresh_token = localStorage.getItem("refresh_token")

    axios.defaults.headers.common["Authorization"] = "Bearer " + refresh_token;
    try{
        let response = await axios.post("https://127:0.0.1:8081/api/user/refresh_token")

        let new_access_token = response.data.access_token 

        localStorage.setItem("access_token", new_access_token)
    } catch(error) {
        // console.error(error)
        this.flashMessage.error({
            message: "error while making new access token"
        });
    }
}


export default refreshAccessToken