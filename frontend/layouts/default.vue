<template>
  <v-app light>
    
   <Navbar/>

    <v-main >
      <Nuxt />
    </v-main>

   
    <v-footer :absolute="!fixed" app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "DefaultLayout",
}
</script>