import { brand, type Lang } from './site';

type ContactCopy = {
  heading: string;
  intro: string;
  emailTitle: string;
  emailAction: string;
  whatsappTitle: string;
  whatsappAction: string;
  phoneTitle: string;
  phoneAction: string;
  externalNotice: string;
  inboxNotice: string;
  previewAnchor: string;
};

export const contactCopy: Record<Lang, ContactCopy> = {
  fr: {
    heading: 'Comment nous joindre',
    intro: 'Pour vos projets, contactez directement l’équipe NextGen par téléphone, e-mail ou WhatsApp.',
    emailTitle: 'Courriel', emailAction: 'Écrire un e-mail',
    whatsappTitle: 'WhatsApp', whatsappAction: 'Ouvrir WhatsApp',
    phoneTitle: 'Téléphone', phoneAction: 'Appeler ce numéro',
    externalNotice: 'E-mail et WhatsApp ouvrent des services externes : l’envoi éventuel est effectué par votre application, et non par le site.',
    inboxNotice: 'Choisissez le moyen de communication qui vous convient.',
    previewAnchor: 'Contacter NextGen',
  },
  ar: {
    heading: 'وسائل التواصل',
    intro: 'لتقديم استفسارك، تواصل مباشرة مع فريق NextGen عبر الهاتف أو البريد الإلكتروني أو واتساب.',
    emailTitle: 'البريد الإلكتروني', emailAction: 'إرسال بريد إلكتروني',
    whatsappTitle: 'واتساب', whatsappAction: 'فتح واتساب',
    phoneTitle: 'الهاتف', phoneAction: 'الاتصال بهذا الرقم',
    externalNotice: 'يُفتح البريد الإلكتروني وواتساب في خدمات خارجية، وأي إرسال يتم عبر تطبيقك وليس عبر الموقع.',
    inboxNotice: 'اختر وسيلة التواصل المناسبة لك.',
    previewAnchor: 'تواصل مع NextGen',
  },
  en: {
    heading: 'Contact channels',
    intro: 'Contact the NextGen team directly by phone, email or WhatsApp.',
    emailTitle: 'Email', emailAction: 'Compose an email',
    whatsappTitle: 'WhatsApp', whatsappAction: 'Open WhatsApp',
    phoneTitle: 'Phone', phoneAction: 'Call this number',
    externalNotice: 'Email and WhatsApp open external services. Any message is sent through your app, not this website.',
    inboxNotice: 'Choose your preferred contact channel.',
    previewAnchor: 'Contact NextGen',
  },
};
/**
 * Contextualized trilingual enquiries open WhatsApp directly, without sending
 * personal information through the NextGen website.
 */
export const productWhatsappHref = (
  lang: Lang,
  product: { code: string; nom: string },
  topic: 'question' | 'documentation' = 'question'
): string => {
  const text = {
    fr: {
      question: 'Bonjour, je souhaite des informations sur la référence',
      documentation: 'Bonjour, je souhaite connaître les documents techniques disponibles pour la référence',
    },
    ar: {
      question: 'مرحبًا، أود الاستفسار عن المرجع',
      documentation: 'مرحبًا، أود معرفة الوثائق الفنية المتاحة للمرجع',
    },
    en: {
      question: 'Hello, I would like information about reference',
      documentation: 'Hello, I would like to know which technical documents are available for reference',
    },
  } satisfies Record<Lang, Record<'question' | 'documentation', string>>;
  const message = `${text[lang][topic]} ${product.nom} (${product.code}).`;
  return `https://wa.me/${brand.whatsapp}?text=${encodeURIComponent(message)}`;
};
