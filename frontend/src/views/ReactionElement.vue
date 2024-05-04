<script>
import axios from "axios";
import {useRoute} from "vue-router";

export default {
    name: "App",
    data() {
      return {
        reaction: {},
      };
    },
    methods: {
      async Response() {
        const { data } = await axios.get("http://amarnathk.pythonanywhere.com/api/reactions?format=json");
        console.log
        const route = useRoute();
        console.log(data)
        for (let i=0;i<=data.length;i++){
            if(data[i]["slug"]==this.$route.params.id) {
              this.reaction = data[i]

            }
        }

      },
      
      
    },
    beforeMount() {
      this.Response();
    },
  };
  </script>
  

<template>
    <h1>{{reaction["name"]}}</h1>
    <div class = "text-black bg-red-400 text-xl max-w-fit p-2 m-4 rounded-sm">{{reaction["conversion"].replace('|', '\u2192')}}</div>
    <p id = 'math' v-for="reactants in reaction['reactants']">\[ \ce{ {{reactants}} ->[ {{ reaction["catalysts"] }}] } \] </p>
    
</template>