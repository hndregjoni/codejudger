<template>
  <v-container style="height: 100%" fluid>
    <v-row style="height: 300px" class="mt-5 py-8 d-flex justify-center">
      <v-col cols="7" align="center">
        <div class="mb-5" style="font-size: 40px">Solve Problems</div>
        <div style="font-size: 20px">
          Here you will find the most <strong>A M A Z I N G</strong> problems and coding challenges .
          <br/>
          It is a given that coding is fun , since you found yourself searching for a coding page.
          The interactive nature of this app, providing with solutions from the community and help from the problem setters themselves is what makes it even more fun . . .
        </div>
      </v-col>
      <v-col   cols="auto" class="d-flex align-center">
        
        <v-row
         
          class="px-5 d-flex justify-content-around"
        >
          <v-icon size="70px"> mdi-language-c </v-icon>
          <v-icon size="70px"> mdi-language-cpp </v-icon>
          <v-icon size="70px"> mdi-language-python </v-icon>
        
     
        
        <v-icon size="70px"> mdi-language-csharp </v-icon>
          <v-icon size="70px"> mdi-language-javascript </v-icon>
          <v-icon size="70px"> mdi-language-haskell </v-icon>
     
      </v-row>


      </v-col>
      
    </v-row>
    <!-- 
        second
     -->
    <v-row style="height: 300px" class="mt-5 py-8 d-flex justify-center">
      <v-col cols="4"  class="d-flex align-center">
        <v-row width="100%" class="px-5 d-flex justify-space-around">
          <v-icon size="70px"> mdi-timer-sand-complete </v-icon>
          <v-icon size="70px"> mdi-gavel </v-icon>
     
          <v-icon size="70px"> mdi-medal </v-icon>
          <v-icon size="70px"> mdi-shimmer </v-icon>
        </v-row>
      </v-col>
      <v-col cols="8" align="center">
        <div class="mb-5" style="font-size: 40px">Participate in contests</div>
        <div style="font-size: 20px">
         If you find yourself a competitive programmer, contests are a great way to prepare yourself for such events.
         <br/>
         Not only you get preparation , but your ranking also increases .
        </div>
      </v-col>
    </v-row>
    <!-- 
   third
 -->

    <v-row style="height: 350px" class="mt-5 py-8 d-flex justify-center">
      <v-col cols="7" align="center">
        <div class="mb-5" style="font-size: 40px">
          Publish your own problems
        </div>
        <div style="font-size: 20px">
          By applying to become a problem setter, you can share problems that
          you have created or problems that you find interesting.
          <br />
          These problems will become part of the contests as well. By
          publishingg your own problems , you can have a peek at solutions in
          different languages.
        </div>
      </v-col>
      <v-col cols="auto" class="d-flex align-center">
        <v-row class="px-7 d-flex justify-space-around">
          <v-icon size="70px"> mdi-file-code </v-icon>

          <v-icon size="70px"> mdi-typewriter </v-icon>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  auth: "guest",
};
</script>
