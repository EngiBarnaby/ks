<template>
    <div class="words-list">
        <div class="columns">
            <div class="column is-4" v-for="word in getUserWords" :key="word.pk">
                <word :word="word" />
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex"
import Word from "../components/words/Word.vue" 
export default {
    name : "Words",

    components : {
        Word
    },

    methods : {
        ...mapActions(["fetchUserWords"])
    },

    computed : {
        ...mapGetters(["getUserWords"])
    },

    async mounted(){
        await this.fetchUserWords()
    }
    
}

</script>
