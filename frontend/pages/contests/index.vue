<template>
    <v-container fluid class="pa-6">
        <v-row class="justify-space-around">
            <v-col justify="center">
                <v-card fill-width>
                    <v-card-title>
                        Problems
                        <v-spacer></v-spacer>
                        <v-text-field v-model="search" append-icon="mdi-magnify" label="Search" single-line
                            hide-details>
                        </v-text-field>
                    </v-card-title>
                    <v-row>
                        <v-select style="width:29%" class="pa-2 ml-3 " :items="['Active', 'Finished']" label="Status"
                            v-model="search">
                        </v-select>
                        <v-select style="width:29%" class="pa-2 mr-3" label="Tags"
                            :items="['Python', 'Java', 'Go', 'Clojure']" v-model="search"></v-select>
                        <v-row class="ml-100">
                            <v-col cols="6" sm="3">
                                <v-menu ref="menu" v-model="menu" :close-on-content-click="false"
                                    :return-value.sync="date" transition="scale-transition" offset-y max-width="200px"
                                    min-width="auto">
                                    <template v-slot:activator="{ on, attrs }">
                                        <v-text-field v-model="date" label="Starts in:" prepend-icon="mdi-calendar"
                                            readonly v-bind="attrs" v-on="on"></v-text-field>
                                    </template>
                                    <v-date-picker v-model="date" no-title scrollable>
                                        <v-spacer></v-spacer>
                                        <v-btn text color="primary" @click="menu = false">
                                            Cancel
                                        </v-btn>
                                        <v-btn text color="primary" @click="$refs.menu.save(date)">
                                            OK
                                        </v-btn>
                                    </v-date-picker>
                                </v-menu>
                            </v-col>
                            <v-spacer></v-spacer>
                            <v-col cols="6" sm="3">
                                <v-menu ref="menu" v-model="menu" :close-on-content-click="false"
                                    :return-value.sync="date" transition="scale-transition" offset-y max-width="200px"
                                    min-width="auto" class="pr-3">
                                    <template v-slot:activator="{ on, attrs }">
                                        <v-text-field v-model="date" label="Ends in:" prepend-icon="mdi-calendar"
                                            readonly v-bind="attrs" v-on="on"></v-text-field>
                                    </template>
                                    <v-date-picker v-model="date" no-title scrollable>
                                        <v-spacer></v-spacer>
                                        <v-btn text color="primary" @click="menu = false">
                                            Cancel
                                        </v-btn>
                                        <v-btn text color="primary" @click="$refs.menu.save(date)">
                                            OK
                                        </v-btn>
                                    </v-date-picker>
                                </v-menu>
                            </v-col>
                        </v-row>
                    </v-row>
                    <v-data-table class="mytab" :headers="headers" :items="contests" :search="search" hide-details>
                    </v-data-table>
                </v-card>
            </v-col>
            <v-col cols="auto">
                <v-card class="pa-2 mb-4">
                    <v-btn block outlined text color="black" class="primary" to="/problems/create" nuxt>
                        Create problem
                    </v-btn>
                </v-card>
                <v-card>

                    <v-date-picker v-model="picker"></v-date-picker>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<style>
.mytab th {
    background-color: rgba(74, 72, 199, 0.493);
}
</style>

<script>

export default {
    data() {


        return {
            picker: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
            search: '',

            headers: [
                {
                    text: 'ID',
                    align: 'start',
                    sortable: false,
                    value: 'id',
                },
                { text: 'Name', value: 'name', sortable: false },
                { text: 'Participants', value: 'participants', sortable: false },
                { text: 'Starts', value: 'stars', sortable: false },
                { text: 'Ends', value: 'end', sortable: false },
            ],
            contests: [

            ],
        }
    },
}
</script>