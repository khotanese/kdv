<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" app>
      <v-list density="compact" nav>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to || undefined"
          :href="item.href || undefined"
          :prepend-icon="item.icon"
          :title="item.title"
        />
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Khotanese Dictionary</v-toolbar-title>
      <v-spacer />
    </v-app-bar>

    <v-main>
      <v-container>
        <slot />
      </v-container>
    </v-main>

    <v-footer app>
      <span>&copy; {{ new Date().getFullYear() }} Khotanese Project | <a href="https://khotanese.org/dictionary/">Content contributors</a> | Webapp was designed by oopus</span>
    </v-footer>
  </v-app>
</template>

<script setup>
const drawer = ref(false)

const items = [
  {
    icon: 'mdi-apps',
    title: 'Khotanese Project',
    href: 'http://khotanese.org/',
  },
  {
    icon: 'mdi-chart-bubble',
    title: 'Khotanese Dictionary',
    to: '/',
  },
  {
    icon: 'mdi-information',
    title: 'About This Dictionary',
    href: 'https://khotanese.org/dictionary/',
  }
]
</script>
