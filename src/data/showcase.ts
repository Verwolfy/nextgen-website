import type { Lang } from './site';

// Existing design renders only. They are not ERP products or validated SKUs.
export const showcaseModels = ['sac-25kg', 'bidon-20l', 'ibc-1000l'] as const;
type Copy = {
  title: string;
  intro: string;
  warning: string;
  simulation: string;
  see3d: string;
  names: readonly [string, string, string];
};
export const showcaseCopy: Record<Lang, Copy> = {
  fr: {
    title: 'Des formats à explorer en 3D',
    intro: 'Découvrez trois maquettes de conditionnements et accédez à la galerie complète de cinq formats.',
    warning: 'Visuels de conception uniquement : emballages, mentions et caractéristiques non approuvés. Aucun produit n’est proposé à la vente.',
    simulation: 'Maquette non validée',
    see3d: 'Voir la galerie 3D',
    names: ['Sac — concept 25 kg', 'Bidon — concept 20 L', 'IBC — concept 1 000 L'],
  },
  ar: {
    title: 'اكتشف تصاميم العبوات ثلاثية الأبعاد',
    intro: 'استعرض ثلاثة نماذج توضيحية للعبوات وانتقل إلى المعرض الكامل الذي يضم خمسة أشكال.',
    warning: 'صور تصميمية فقط: العبوات والبيانات والمواصفات غير معتمدة. لا تمثل هذه النماذج منتجات معروضة للبيع.',
    simulation: 'نموذج غير معتمد',
    see3d: 'استعرض المعرض ثلاثي الأبعاد',
    names: ['كيس — نموذج 25 كغ', 'عبوة — نموذج 20 لترًا', 'خزان IBC — نموذج 1000 لتر'],
  },
  en: {
    title: 'Explore packaging in 3D',
    intro: 'Preview three illustrative packaging designs, then explore the full five-format gallery.',
    warning: 'Design concepts only: packaging, labels and specifications are not approved. No products are offered for sale.',
    simulation: 'Unapproved concept',
    see3d: 'Explore the 3D gallery',
    names: ['Bag — 25 kg concept', 'Jerrycan — 20 L concept', 'IBC tote — 1,000 L concept'],
  },
};
