<template>
  <v-app  light>
    
    <v-app-bar
      app
      color="primary"
      flat
    >
      <v-container class="py-0 fill-height">
        <v-avatar
          class="mr-10"
          color="info"
          size="32"
        >CJ</v-avatar>

       <v-menu
        v-for="text in links"
        :key="text"
        offset-y
       >

      <template v-slot:activator="{ attrs, on }"  >
       

          <v-btn 
          text 
          v-bind="attrs"
          v-on="on">
                  {{ text }}
          </v-btn>
   
      </template>

      <v-list  color="deep-purple lighten-5">
        <v-list-item
           
          v-for="item in items"
          :key="item"
          link
        >
          <v-list-item-title v-text="item" class="black--text"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

        <v-spacer></v-spacer>

        <v-responsive max-width="260" >
          <v-text-field 
            dense
            flat
            hide-details
            rounded
            filled
            class="white"
            
          ></v-text-field>
        </v-responsive>
      </v-container>
    </v-app-bar>

    <v-main >
      <v-container align-items: center fill-width>
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

<script>
export default {
  name: 'DefaultLayout',
 
    data: () => ({
      links: [
        'Dashboard',
        'Messages',
        'Profile',
        'Updates',
      ],
   
      items: [...Array(4)].map((_, i) => `Item ${i}`),
    }),
 
}
</script>

