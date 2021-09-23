<template>
    <div class="box ml-1">
        <div class="content">
            <h5 class="has-text-centered">
                {{ word.content }}
            </h5>
            <div class="add-word">
                <span class="icon is-size-4 has-text-grey"><i class="fas fa-plus"></i></span>
            </div>
            <p class="has-text-centered word">
                Translate
            </p>

            <div
                class="word-list"
                 v-for="(wordTranslate, index) in translateList" :key="index">
                 <p>{{wordTranslate.part_of_speech}}: <span class="has-text-weight-medium">{{wordTranslate.translate}}</span></p>
            </div>
            <div class="columns mt-2">
                <div class="column is-8">
                    <div class="field">
                        <div class="control">
                            <input 
                                class="input is-success" 
                                type="text" 
                                placeholder="Success input"
                                v-model="translate"
                                >
                        </div>
                    </div>
                </div>
                <div class="column is-4">
                    <div class="control">
                        <div class="select">
                            <select  v-model="part_of_speech">
                                <option>noun</option>
                                <option>pronoun</option>
                                <option>verb</option>
                                <option>adjective</option>
                                <option>adverb</option>
                                <option>preposition</option>
                                <option>conjunction</option>
                                <option>interjection</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            <div class="has-text-centered">
                <button 
                    class="button is-info is-light"
                    @click="addNewTranslate"
                >
                    Add translate
                </button>
            </div>
        </div>
    </div>
</template>


<script>
import { mapActions } from "vuex"
export default {
    props : {
        word : {
            type : Object,
            required : true,
        }
    },

    name : "WordList",

    data(){
        return {
            translateList : this.word.words_translate,
            translate : "",
            part_of_speech: "",
        }
    },

    methods : {
        ...mapActions(["addWordTranslate"]),
        addNewTranslate(){
            let data = { "translate" : this.translate, "part_of_speech" : this.part_of_speech, "word" : this.word.id}
            this.addWordTranslate(data)
                .then(responce => {
                    this.translateList.push(responce.data)
                })
        }
    },
}
</script>

<style lang="scss">

.box {
    position: relative;
    border: 1px solid rgb(112, 135, 153);
}

.word {
    border-bottom: 1px solid black;
}

.word-list {
    margin-bottom: 1px;
}

.add-word {
    position: absolute;
    // width: 40px;
    // height: 30px;
    // border: 1px solid rgb(112, 135, 153);
    top:  5px;
    left: 5px;
    padding-left: 3px;
}

.add-word:hover{
    cursor: pointer;
}

</style>
