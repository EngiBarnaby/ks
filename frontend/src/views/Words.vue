<template>
    <div class="words-list">
        <div class="columns is-multiline">
            <div class="column is-3" v-for="word in getUserWords" :key="word.pk">
                <word :word="word" />
            </div>
        </div>

        <button class="button" @click="prevWords">
            Prev
        </button>
        
        <button class="button" @click="nextWords">
            Next
        </button>
        
    </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex"
import Word from "../components/words/Word.vue" 
export default {
    name : "Words",

    props : ["page"],

    components : {
        Word
    },

    data(){
        return {
            page_size : 3
        }
    },

    methods : {
        ...mapActions(["fetchUserWords", "nextWords", "prevWords"])
    },

    computed : {
        ...mapGetters(["getUserWords"])
    },

    async created(){
        await this.fetchUserWords({"pageNum" : this.page, "page_size" : this.page_size})
    }
    
}

</script>
