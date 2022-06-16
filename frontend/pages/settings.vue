<template>
<div class="fill-height" style=" display: flex;
  flex-direction: row; ">
  <div >
    <v-container fill-height  >

      <v-card height="100%" width="256">
      <v-navigation-drawer permanent>
        <v-list>
          <v-list-item
            v-for="item in items"
            :key="item.title"
            :to="item.url"
            nuxt
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              {{ item.title }}
            </v-list-item-content>
          </v-list-item>
        </v-list>

        <template v-slot:append>
          <div class="pa-2">
            <v-btn block> Logout </v-btn>
          </div>
        </template>
      </v-navigation-drawer>
    </v-card>
    
</v-container>
</div>

    <v-container fill-height fluid >
    
      <NuxtChild />
   
    </v-container>

   
    </div>
 
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          title: "View metrics ",
          icon: "mdi-view-dashboard",
          url: "/settings/metrics",
        },
        {
          title: "Manage users",
          icon: "mdi-account-box",
          url: "/settings/user",
        },
        {
          title: "Approve requests ",
          icon: "mdi-gavel",
          url: "/settings/requests",
        },
         {
          title: "Problems ",
          icon: "mdi-bookmark-plus",
          url: "/settings/problem",
        },
         {
          title: "Manage languages ",
          icon: "mdi-translate",
          url: "/settings/languages",
        },
      ],
    };
  },
};
</script>