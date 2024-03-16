<template>
    <div>
        <Header :query="query_in_home"></Header>
        "hey! I am in Home.vue"

        <!-- <div v-for="user in all_users_data" :key="user.user_id" v-show="all_users_data">
        {{ user.user_mail }}
    </div> -->
        <input v-model="query_in_home" v-on:input="search_in_home()">
        <b-container>
            <b-row>
                <b-col v-show="all_users_data_searched" v-for="user in all_users_data_searched" :key="user.user_id"
                    col="12" md="4" style="margin: 10px;">
                    <b-list-group>
                        <b-list-group-item>User_id = {{ user.user_id }}</b-list-group-item>
                        <b-list-group-item>Password = {{ user.password.slice(0, 10) }}</b-list-group-item>
                        <b-list-group-item>user_email = {{ user.user_mail }}</b-list-group-item>
                    </b-list-group>
                </b-col>
            </b-row>
        </b-container>



    </div>
</template>

<script>
import axios from 'axios'
import Header from '@/components/Header.vue'
import refreshAccessToken from '@/utils/refreshToken'

export default {
    name: 'UserHome',
    components: {
        Header
    },
    data() {
        return {
            all_users_data_searched: [],
            all_users_data: {},
            query_in_home: "",
            x: true
        }
    },
    methods: {
        logoutUser() {
            localStorage.removeItem("access_token")
            localStorage.removeItem("refresh_token")
            localStorage.removeItem("user_mail")

            alert("user log out!!!!")
            this.$router.push("/login")
        },
        search_in_home() {
            let query = this.query_in_home.toLocaleLowerCase()
            if (!query) {
                this.all_users_data_searched = this.all_users_data
            }
            else if (query) {
                this.all_users_data_searched = []
                for (let user of this.all_users_data) {
                    if (user.user_mail.toLocaleLowerCase().includes(query)) {

                        this.all_users_data_searched.push(user)
                    }

                    else if (user.password.toLocaleLowerCase().includes(query)) {

                        this.all_users_data_searched.push(user)
                    }
                }
            }
        },
        async getAllUserData() {
            try {
                let access_token = localStorage.getItem('access_token')
                // let user_id = localStorage.getItem('user_id')

                axios.defaults.headers.common['Authorization'] = 'Bearer ' + access_token
                const dataResponse = await axios.get(`http://127.0.0.1:8081/api/user`)

                this.all_users_data_searched = dataResponse.data
                this.all_users_data = dataResponse.data

                this.flashMessage.success({
                    message: "user data retrieved"
                });


            }
            catch (error) {
                if (error.response && error.response.status == 401) {
                    await refreshAccessToken();
                    await this.getAllUserData();
                    this.flashMessage.success({
                        message: "new token made"
                    });

                }
                else if (error.response) {
                    this.flashMessage.error({
                        message: "error error bye bye"
                    });
                }

            }
        }
    },
    created() {
        this.getAllUserData()
    }

}
</script>

<style scoped></style>