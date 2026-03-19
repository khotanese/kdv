<template>
  <v-app>
    <v-container class="text-center mt-10">
      <h1 v-if="error.statusCode === 404">404 Not Found</h1>
      <h1 v-else>An error occurred</h1>
      <NuxtLink to="/">Home page</NuxtLink>
    </v-container>
  </v-app>
</template>

<script setup>
defineProps({
  error: Object
})
</script>

<style scoped>
h1 {
  font-size: 20px;
}
</style>
