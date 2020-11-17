<template>
 <div>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <div class="text-center">
        <v-text-field
          label="Type your word"
           v-model="search_term"
           v-on:keyup.enter="call_search_api"
        ></v-text-field>

        <v-btn
          class="mr-4"
          v-on:click="call_search_api"
        >
          Search
        </v-btn>
        <v-btn
          class="mr-4"
          v-on:click="clear_search_box"
        >
          Clear
        </v-btn>
      </div><br />
          <v-list>
            <v-list-item v-for="word_item in search_result_items" :key="word_item.id">
              <v-card style="width:600px">
              <v-card-title class="headline">{{word_item.word}}</v-card-title>
              <!-- <v-card-text><p v-html="word_item.content">{{word_item.content}}</p></v-card-text> -->
              <v-card-text><p v-html="word_item.content"></p></v-card-text>
              </v-card>
            </v-list-item>
          </v-list>      
    </v-col>
  </v-row>
 </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      search_term: "",
      search_result_items: [],
    }
  },
  methods: {
    clear_search_box: function () {
      this.search_term = "";
    },
    call_search_api: function(){
      let query_url = "https://oopus.info/kd/index.php?term=" + this.search_term;
      let _this = this;
      _this.search_result_items = [{word:"Searching...", content: "", id: 0}]
      axios.get(query_url)
      .then(function (response) {
        _this.search_result_items = response.data;
      }).catch(function (error) {
        console.log(error);
      });
    }
  }
}
</script>


