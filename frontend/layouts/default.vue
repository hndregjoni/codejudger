<template>
  <v-app dark>
    
   <Navbar/>

    <v-main >

      <v-container  style="align-items: center" fill-width>
        <Nuxt />
      </v-container>
    </v-main>

    <v-navigation-drawer
      v-model="rightDrawer"
      :right="right"
      temporary
      fixed
    >
      <v-list>
        <v-list-item @click.native="right = !right">
          <v-list-item-action>
            <v-icon light>
              mdi-repeat
            </v-icon>
          </v-list-item-action>
          <v-list-item-title>Switch drawer (click me)</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-footer
      :absolute="!fixed"
      app
    >
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>
<style >
.theme--dark.v-application {
  background-color: var(--v-background-base) !important;
}
.theme--light.v-application {
  background-color: var(--v-background-base) !important;
}
</style>

<script>
export default {
  name: 'DefaultLayout',
  components:true
}
</script>

