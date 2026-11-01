import type { Lang } from './site';

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
    intro: 'Les demandes en ligne intégrées au site ne sont pas activées. Vous pouvez ouvrir les coordonnées indiquées ci-dessous dans votre application habituelle.',
    emailTitle: 'Courriel', emailAction: 'Écrire un e-mail',
    whatsappTitle: 'WhatsApp', whatsappAction: 'Ouvrir WhatsApp',
    phoneTitle: 'Téléphone', phoneAction: 'Appeler ce numéro',
    externalNotice: 'E-mail et WhatsApp ouvrent des services externes : l’envoi éventuel est effectué par votre application, et non par le site.',
    inboxNotice: 'La réception effective des messages par ces coordonnées n’a pas été vérifiée dans cette préproduction.',
    previewAnchor: 'Voir le modèle de demande (désactivé)',
  },
  ar: {
    heading: 'وسائل التواصل',
    intro: 'لم تُفعَّل استمارات الطلب عبر الموقع. يمكنك فتح وسائل الاتصال التالية باستخدام تطبيقاتك المعتادة.',
    emailTitle: 'البريد الإلكتروني', emailAction: 'إرسال بريد إلكتروني',
    whatsappTitle: 'واتساب', whatsappAction: 'فتح واتساب',
    phoneTitle: 'الهاتف', phoneAction: 'الاتصال بهذا الرقم',
    externalNotice: 'يُفتح البريد الإلكتروني وواتساب في خدمات خارجية، وأي إرسال يتم عبر تطبيقك وليس عبر الموقع.',
    inboxNotice: 'لم يتم التحقق من استقبال الرسائل فعليًا عبر هذه البيانات في النسخة التجريبية.',
    previewAnchor: 'عرض نموذج الطلب غير المفعل',
  },
  en: {
    heading: 'Contact channels',
    intro: 'The website enquiry forms are not active. You can open the contact details below using your usual applications.',
    emailTitle: 'Email', emailAction: 'Compose an email',
    whatsappTitle: 'WhatsApp', whatsappAction: 'Open WhatsApp',
    phoneTitle: 'Phone', phoneAction: 'Call this number',
    externalNotice: 'Email and WhatsApp open external services. Any message is sent through your app, not this website.',
    inboxNotice: 'Actual message delivery to these contact details has not been verified in this preproduction.',
    previewAnchor: 'View the disabled enquiry preview',
  },
};
