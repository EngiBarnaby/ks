<template>
    <div>
        <div class="columns mt-6">
            <div class="column is-4 is-offset-4 box">

                <div class="content">
                    <h1 class="has-text-centered">
                        Sign Up
                    </h1>
                </div>

                <form v-on:submit.prevent="submitForm">
                    <div class="field">
                        <label  class="lable">Email</label>
                        <div class="control">
                            <input type="email" class="input" v-model="email">
                        </div>
                        <p class="help">Write your email</p>
                    </div>

                    <div class="field">
                        <label  class="lable">Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                        <p class="help">Write your password</p>
                    </div>


                    <div class="has-text-centered">
                        <button class="button is-info is-medium">Login</button>
                    </div>
                </form>

            </div>
        </div>
    </div>
</template>

<script>
import { mapActions, mapMutations  } from "vuex"
export default {
    name : "LoginUser",

    data(){
        return {
            email : "",
            password : "",
        }
    },

    methods : {
        ...mapActions(["loginUser"]),
        ...mapMutations(["setUserName", "setAthenticated"]),
        submitForm(){
            this.loginUser({email: this.email, password: this.password})
            .then( () => {
                this.setUserName()
                this.setAthenticated()
                this.$router.push("/")
            })
            .catch( error => console.log(error))
        }
    }
}

</script>