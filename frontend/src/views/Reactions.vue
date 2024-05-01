
<script>
import axios from "axios";

export default {
    name: "App",
    data() {
      return {
        reactions: {},
      };
    },
    methods: {
      async Response() {
        const { data } = await axios.get("http://localhost:8000/api/reactions?format=json");
        this.reactions = data;

      },
      
    },
    beforeMount() {
      this.Response();
    },
  };
</script>

<template>
    <h1>Reactions</h1>
    <p>List of available reactions in the database. Clicking on any of these will take you to a unique page for that reaction.</p>
    <div class = "list-decimal pl-9" ><li v-for="reaction in reactions" id = "app"> <router-link class = "text-inherit no-underline hover:text-blue-300" :to="'reactions/'+reaction.slug" >{{ reaction["name"] }}</router-link></li></div>
    
    
</template>