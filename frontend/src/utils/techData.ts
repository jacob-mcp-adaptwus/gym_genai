import { shallowRef } from 'vue';

//assets
import tech1 from '@/assets/images/landing/tech-bootstrap.svg';
import tech2 from '@/assets/images/landing/tech-react.svg';
import tech3 from '@/assets/images/landing/tech-angular.svg';
import tech4 from '@/assets/images/landing/tech-codeigniter.svg';
import tech5 from '@/assets/images/landing/tech-net.svg';
// import tech6 from '@/assets/images/landing/tech-figma.svg';
import tech7 from '@/assets/images/landing/tech-nextjs.svg';
import tech8 from '@/assets/images/landing/tech-vuetify.svg';
import tech9 from '@/assets/images/landing/tech-vue-laravel.svg';
import tech10 from '@/assets/images/landing/tech-django.svg';
import tech11 from '@/assets/images/landing/tech-flask.svg';
import tech12 from '@/assets/images/landing/tech-node.svg';
import tech13 from '@/assets/images/landing/tech-laravel.svg';
import tech14 from '@/assets/images/landing/tech-svelte.svg';
import tech15 from '@/assets/images/landing/tech-tailwind.svg';

const techData = shallowRef([
  {
    title: 'Tailwind',
    image: tech15,
    link: 'https://ableproadmin.com/tailwind/dashboard/index.html',
    target: '_blank',
    name: 'Click to preview Tailwind',
    description:
      "Able Pro with Tailwind CSS lets developers create sleek, professional interfaces quickly. Tailwind's utility classes ensure consistent styling across all devices",
    free: null
  },
  {
    image: tech1,
    title: 'Bootstrap 5',
    target: '_blank',
    name: 'Click to preview Bootstrap 5',
    description:
      'Able Pro Bootstrap 5 - the top choice for responsive, mobile-first design, you can achieve both professional functionality and visual appeal.',
    link: 'https://ableproadmin.com/dashboard/index.html',
    free: 'https://github.com/phoenixcoded/able-pro-free-admin-dashboard-template'
  },
  {
    image: tech2,
    title: 'React MUI',
    target: '_blank',
    name: 'Click to preview React',
    description:
      'Able Pro React dashboard template is a powerful tool that utilizes the Material-UI component library to create stunning and intuitive user interfaces.',
    link: 'https://ableproadmin.com/react/dashboard/default',
    free: 'https://github.com/phoenixcoded/able-pro-free-admin-dashboard-template',
    label: 'trending'
  },
  {
    image: tech4,
    title: 'Codeigniter',
    target: '_blank',
    name: 'Click to preview Codeigniter',
    description:
      'Able Pro CodeIgniter version is a powerful dashboard template built specifically for developers who use the CodeIgniter PHP framework with Bootstrap.',
    link: 'https://ableproadmin.com/codeigniter/default/public/dashboard-default',
    free: null
  },
  {
    image: tech5,
    title: 'ASP.net',
    target: '_blank',
    name: 'Click to preview ASP.net',
    description:
      'Able Pro .NET version is a robust dashboard template designed specifically for .NET developers. Its comes with a wide range of pre-built components.',
    link: 'https://able-pro.azurewebsites.net/Dashboard/Index',
    free: null
  },
  {
    image: tech3,
    title: 'Angular',
    target: '_blank',
    name: 'Click to preview Angular',
    description:
      'Able Pro Angular dashboard template is a powerful tool that utilizes the Google Material component library to create stunning and intuitive user interfaces.',
    link: 'https://ableproadmin.com/angular/default/dashboard/default',
    free: 'https://github.com/phoenixcoded/able-pro-free-admin-dashboard-template'
  },
  {
    image: tech7,
    title: 'Next.js',
    target: '_blank',
    name: 'Click to preview Nextjs',
    description:
      'Able Pro Next Js dashboard template is a powerful tool that utilizes the Mate,rial-UI component library to create stunning and intuitive user interfaces.',
    link: 'https://able-pro-material-next-ts-navy.vercel.app/dashboard/default',
    free: null
  },
  {
    image: tech8,
    title: 'Vue',
    target: '_blank',
    name: 'Click to preview Vuetify',
    description:
      'Able Pro Vue stands out as a versatile and powerful - Vue with Vuetify dashboard combines modern design principles with robust functionality.',
    link: 'https://ableproadmin.com/vue/dashboard/default',
    free: 'https://github.com/phoenixcoded/able-pro-free-admin-dashboard-template'
  },
  // {
  //   image: tech6,
  //   title: 'Figma',
  //   target: '_blank',
  //   name: 'Figma design system',
  //   description:
  //     'Able Pro comes with a Figma design file that allows you to customize and fine-tune your dashboard to meet your specific needs.',
  //   link: 'https://www.figma.com/file/6XqmRhRmkr33w0EFD49acY/Able-Pro--v9.0-Figma-Preview?type=design&node-id=46-226114&mode=design&t=1gF4FHiDzpwHzoMs-0',
  //   free: null
  // },
  {
    image: tech9,
    title: 'Vuetify Laravel',
    target: '_blank',
    name: 'Click to preview Vuetify with Laravel',
    description: `Able Pro Vue stands out as a versatile and powerful - Vue with Vuetify dashboard combines modern design principles with robust functionality.`,
    link: 'https://phplaravel-207002-4524103.cloudwaysapps.com/build/dashboards/default',
    free: null
  },
  {
    image: tech10,
    title: 'Django',
    target: '_self',
    description:
      'Able Pro Django is a powerful dashboard template designed for developers. it offers an extensive collection of pre-built components for seamless web development.',
    name: 'Live Preview not available',
    free: null
  },
  {
    image: tech11,
    title: 'Flask',
    target: '_self',
    description:
      'Able Pro Flask is a versatile dashboard solution that offers a rich set of pre-built components to simplify web development.',
    name: 'Live Preview not available',
    free: null
  },
  {
    image: tech12,
    title: 'NodeJS',
    target: '_self',
    description:
      'Able Pro Node.js combines flexibility and functionality with a variety of pre-built components tailored for Node.js, which make it easier to develop.',
    name: 'Live Preview not available',
    free: null
  },
  {
    image: tech13,
    title: 'Laravel',
    target: '_self',
    description:
      'Able Pro Laravel with Bootstrap provides a powerful set of tools and components, crafted specifically for Laravel, to simplify and accelerate your development process.',
    name: 'Live Preview not available',
    free: null
  },
  {
    image: tech14,
    title: 'Svelte',
    target: '_self',
    description:
      'Able Pro Svelte provides an extensive toolkit and components, allowing you to build dynamic and responsive interfaces with ease and efficiency.',
    name: 'Live Preview not available',
    free: null
  }
]);

export default techData;
