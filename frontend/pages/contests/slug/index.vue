<template >

    <div class=" my-5">
        <v-col cols="12" md="12">
            <div :class="`rounded-br-xl`" class="py-5  text-center primary ">
                <label class="white--text"> <b>Contest name </b> </label>
            </div>
        </v-col>
        <v-col align="center" class="justify-center py-6">
            <v-chip class="ma-1 primary" text-color="white">
                <v-icon left>
                    mdi-label
                </v-icon>
                Tag1
            </v-chip>
            <v-chip class="ma-1  primary" text-color="white">
                <v-icon left>
                    mdi-label
                </v-icon>
                Tag2
            </v-chip>
            <v-chip class="ma-1  primary" text-color="white">
                <v-icon left>
                    mdi-label
                </v-icon>
                Tag3
            </v-chip>
            <v-chip class="ma-1 primary" text-color="white">
                <v-icon left>
                    mdi-label
                </v-icon>
                Tag4
            </v-chip>
            <v-chip class="ma-1 primary" text-color="white">
                <v-icon left>
                    mdi-label
                </v-icon>
                Tag5
            </v-chip>
            <v-row class="mt-5 mx-15">
                <v-textarea class="mx-10" filled outlined readonly value="First problem"></v-textarea>
                <v-btn   class="mx-10 mt-10 primary" dense flat> Solve </v-btn>
            </v-row>
                        <v-row class="mt-5 mx-15">
                <v-textarea class="mx-10" filled outlined readonly value="Probelm#2"></v-textarea>
                <v-btn   class="mx-10 mt-10 primary" dense flat> Solve </v-btn>
            </v-row>
                        <v-row class="mt-5 mx-15">
                <v-textarea class="mx-10" filled outlined readonly value="Problem#3"></v-textarea>
                <v-btn   class="mx-10 mt-10 primary" dense flat> Solve </v-btn>
            </v-row>
                        <v-row class="mt-5 mx-15">
                <v-textarea class="mx-10" filled outlined readonly value=" Problem#4"></v-textarea>
                <v-btn   class="mx-10 mt-10 primary" dense flat> Solve </v-btn>
            </v-row>
        </v-col>
       
    </div>
</template>

<script>
export default {
    data() {
        return {

        }
    }
}
</script>