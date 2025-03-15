export interface menu {
  header?: string;
  title?: string;
  icon?: string;
  to?: string;
  divider?: boolean;
  getURL?: boolean;
  chip?: string;
  chipColor?: string;
  chipVariant?: string;
  chipIcon?: string;
  children?: menu[];
  disabled?: boolean;
  type?: string;
  subCaption?: string;
}
const sidebarItem: menu[] = [
  { header: 'Mathtilda' },
  {
    title: 'Lessons',
    icon: 'custom-home-trend',
    to: '/dashboard/default',
    children: [
      {
        title: 'My Plans',
        to: '/plans/myplans'
      }
    ]
  },
  {
    title: 'My Profiles',
    icon: 'profile',
    to: '/profiles/myprofiles'
  },
];

export default sidebarItem;
