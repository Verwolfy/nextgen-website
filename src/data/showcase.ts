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
    warning: 'Visualisation 3D des formats d’emballages FENEK.',
    simulation: 'Modèle 3D',
    see3d: 'Voir la galerie 3D',
    names: ['Sac — concept 25 kg', 'Bidon — concept 20 L', 'IBC — concept 1 000 L'],
  },
  ar: {
    title: 'نماذج مقترحة للعبوات بتقنية ثلاثية الأبعاد',
    intro: 'شاهد ثلاثة تصاميم توضيحية، ثم انتقل إلى المعرض الذي يضم خمسة أنواع من العبوات.',
    warning: 'استكشف نماذج عبوات FENEK ثلاثية الأبعاد.',
    simulation: 'نموذج ثلاثي الأبعاد',
    see3d: 'عرض جميع النماذج ثلاثية الأبعاد',
    names: ['كيس — نموذج بوزن 25 كغ', 'عبوة سائلة — نموذج بسعة 20 لترًا', 'خزان IBC — نموذج بسعة 1,000 لتر'],
  },
  en: {
    title: 'Explore packaging in 3D',
    intro: 'Preview three illustrative packaging designs, then explore the full five-format gallery.',
    warning: 'Explore the FENEK packaging formats in 3D.',
    simulation: '3D model',
    see3d: 'Explore the 3D gallery',
    names: ['Bag — 25 kg concept', 'Jerrycan — 20 L concept', 'IBC tote — 1,000 L concept'],
  },
};
