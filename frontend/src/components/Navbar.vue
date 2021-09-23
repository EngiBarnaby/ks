<template>
    <div class="main-nav-bar">
        <nav class="navbar" role="navigation" aria-label="main navigation">
            <div class="navbar-brand">
                <a class="navbar-item" href="https://bulma.io">
                <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
                </a>

                <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                </a>
            </div>

            <div id="navbarBasicExample" class="navbar-menu">
                <div class="navbar-start">
                <a class="navbar-item" href="/">
                    Home
                </a>

                <a class="navbar-item">
                    Api
                </a>
                <a class="navbar-item" href="/words">
                    Words
                </a>
                <div class="navbar-item has-dropdown is-hoverable">
                    <a class="navbar-link">
                    More
                    </a>

                    <div class="navbar-dropdown">
                    <a class="navbar-item">
                        About
                    </a>
                    <a class="navbar-item">
                        Jobs
                    </a>
                    <a class="navbar-item">
                        Contact
                    </a>
                    <hr class="navbar-divider">
                    <a class="navbar-item">
                        Report an issue
                    </a>
                    </div>
                </div>
                </div>

                <div class="navbar-end">
                <div class="navbar-item">

                    <a class="navbar-item">
                        {{ getUserName }}
                    </a>
                    <div class="buttons" v-if="!getIsAuthenticated">
                        <a class="button is-primary" href="/sign-up">
                            <strong>Sign up</strong>
                        </a>
                        <a class="button is-light" href="/login">
                            Log in
                        </a>
                    </div>
                    <div class="buttons" v-else-if="getIsAuthenticated" @click="userLogOut">
                        <button class="button" href="/sign-up">
                            <strong>Log out</strong>
                        </button>
                    </div>
                </div>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex"
export default {
    name : "Navbar",
    
    computed : {
        ...mapGetters(["getUserName", "getIsAuthenticated"])
    },

    methods : {
        ...mapActions(["logOut"]),
        userLogOut(){
            this.logOut()
        }
    }
}
</script>