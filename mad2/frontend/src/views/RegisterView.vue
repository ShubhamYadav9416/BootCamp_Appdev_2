<template>
    <div>
        <Header></Header>
        <b-container class="bv-example-row">
            <b-row>
                <b-col>1 of 3</b-col>
                <b-col>
                    <h1>register Page</h1>

                    <b-form>
                        <b-form-group id="input-group-1" label="Email address:" label-for="input-1"
                            description="We'll never share your email with anyone else.">
                            <b-form-input id="input-1" v-model="form.email" type="text" placeholder="Enter email"
                                required></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-group-2" label="Your Password:" label-for="input-2">
                            <b-form-input id="input-2" v-model="form.password" placeholder="Enter Password"
                                required></b-form-input>
                        </b-form-group>
                        <b-form-group id="input-group-2" label="Your Re-Password:" label-for="input-2">
                            <b-form-input id="input-2" v-model="form.re_password"  placeholder="Enter Password again"
                                required></b-form-input>
                        </b-form-group>
                        <b-button type="button" variant="primary" @click="registerUser()">Submit</b-button>
                        <b-button type="reset" variant="danger" @click="resetForm()">Reset</b-button>
                    </b-form>
                    <b-card class="mt-3" header="Form Data Result">
                        <pre class="m-0">{{ form }}</pre>
                    </b-card></b-col>
                <b-col>3 of 3</b-col>
            </b-row>
        </b-container>
    </div>
</template>



<script>

import axios from 'axios';
import Header from '@/components/Header.vue';

export default {
    name: 'RegisterUserView',
    components: {
        Header
    },
    data() {
        return {
            form: {
                email: "",
                password: "",
                re_password:""
            }

        }
    },
    methods: {
        resetForm() {
            this.form.email = "";
            this.form.password = "";
            this.form.re_password=""
        },
        registerUser() {

            if(!this.form.email || !this.form.password || !this.form.re_password){
                alert("All fields are required")
                return;
            }

            if(!this.form.email.includes("@") || !this.form.email.endsWith(".com")){
                alert("invalid email");
                return;
            }

            if (this.form.password != this.form.re_password){
                alert("Password don't match!!!!!!!!!!!!!")
                return;
            }

            axios.post("http://127.0.0.1:8081/api/user/register",{
                user_mail : this.form.email,
                password: this.form.password,
            })
            .then((response) => {
                if (response.data.status == "success"){
                    alert(response.data.message)
                    this.$router.push('/login')
                }
                if (response.data.status == "failed"){
                    alert(response.data.message)
                }

            })
            .catch((error) => {
                console.error(error);
                alert("An error occurred  while registering")
            })

        }
    }
}

</script>




<style scoped></style>