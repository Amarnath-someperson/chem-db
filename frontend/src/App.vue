
<template>
  <div class = "flex justify-start m-10 max-sm:flex-col max-sm:mt-0 ">
    <nav class = "flex-grow p-4 basis-1/5 max-w-72 max-sm:flex-auto bg-gray-800 shadow-md max-sm:mt-0">
      <div class = "text-blue-400 mb-4 font-thin">Viewing {{ $route.fullPath}}</div>
      <div class = " mb-3 "><router-link class = "text-green-400 font-bold no-underline text-3xl hover:text-green-200" to="/">Home</router-link> </div>
      <div class = mb-3><router-link  class = "text-green-400 font-bold no-underline text-3xl hover:text-green-200" to="/reactions">Reaction Library</router-link></div>

      <q>A universe of atoms, an atom in the universe.</q>
    </nav>
    <main class = "flex-grow m-2 p-2 basis-4/5 max-w-4xl max-sm:flex-auto">
      <router-view/>
    </main>
  </div>

</template>

