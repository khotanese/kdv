<template>
  <div>
    <v-row justify="center" align="center">
      <v-col cols="12" sm="8" md="6">
        <div class="text-center">
          <v-text-field
            label="Type your word"
            v-model="search_term"
            @keyup.enter="call_search_api"
          />

          <v-btn class="mr-4" @click="call_search_api">
            Search
          </v-btn>
          <v-btn class="mr-4" @click="search_term = ''">
            Clear
          </v-btn>
        </div>
        <br />
        <v-list>
          <v-list-item v-for="word_item in search_result_items" :key="word_item.id">
            <v-card style="width: 600px">
              <v-card-title class="text-h6">{{ word_item.word }}</v-card-title>
              <v-card-text>
                <p v-html="word_item.content_style_with_link"></p>
              </v-card-text>
            </v-card>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>
  </div>
</template>

<script setup>
const search_term = ref('')
const search_result_items = ref([])

async function call_search_api() {
  search_result_items.value = [{ word: 'Searching...', content_style_with_link: '', id: 0 }]
  try {
    const data = await $fetch(`https://oopus.info/kd/index.php?term=${search_term.value}`)
    search_result_items.value = data
  } catch (error) {
    console.log(error)
  }
}
</script>
