import axios  from "@/plugins/axios"

const wordsStore = {
    state: {
        userWords : [],
    },

    mutations: {
        setUserWords(state, data) {
            state.userWords = data
        }
    },

    actions: {
        async fetchUserWords(context) {
            let { data } = await axios.get("/api/words-list-test/")
            console.log(data);
            context.commit("setUserWords", data)
        }
    },

    getters: {
        getUserWords : state => state.userWords
    }
}

export default wordsStore;