<template>
  <v-app light>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          :href="item.href"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      :clipped-left="clipped"
      fixed
      app
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title v-text="title" />
      <v-spacer />
    </v-app-bar>
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>

    <v-footer
      :absolute="!fixed"
      app
    >
      <span>&copy; {{ new Date().getFullYear() }} Khotanese Project | <a href="https://khotanese.org/khotanese-dictionary/">Content contributors</a> | Webapp was designed by oopus</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data () {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Khotanese Project',
          to: '',
          href: 'http://khotanese.org/',
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Khotanese Dictionary',
          to: '/'
        },
        {
          icon: 'mdi-apps',
          title: 'About This Dictionary',
          to: '',
          href: 'https://khotanese.org/dictionary/'
        }
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Khotanese Dictionary'
    }
  }
}
</script>
