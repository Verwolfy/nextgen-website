import type { Lang } from './site';
export type LeadKind = 'quote' | 'distributor';
export const fieldOrder: Record<LeadKind, readonly string[]> = {
  quote: ['business', 'contact', 'phone', 'email', 'wilaya', 'commune', 'product', 'package', 'quantity', 'message'],
  distributor: ['business', 'contact', 'phone', 'email', 'wilaya', 'commune', 'activity', 'brands', 'message'],
};
export type FieldKey = (typeof fieldOrder)['quote'][number] | (typeof fieldOrder)['distributor'][number];
type Copy = { title: Record<LeadKind,string>; intro:Record<LeadKind,string>; disabled:string; privacy:string; consent:string; send:string; alternative:string; fields:Record<FieldKey,string> };
export const leadCopy: Record<Lang,Copy> = {
  fr: {
    title: { quote:'Demande de devis',distributor:'Candidature distributeur' },
    intro: { quote:'Décrivez votre besoin afin de préparer une future demande commerciale.',distributor:'Présentez votre entreprise pour rejoindre notre futur réseau de distribution.' },
    disabled:'Formulaire de démonstration — envoi désactivé. Aucune donnée saisie ici n’est recueillie ni transmise.',
    privacy:'Les formalités de confidentialité et le circuit CRM doivent être validés avant activation des formulaires.',
    consent:'J’ai lu la politique de confidentialité et j’autorise le traitement de cette demande.',
    send:'Envoyer la demande',alternative:'Pour nous contacter dès maintenant, utilisez l’e-mail ou WhatsApp.',
    fields: {business:'Entreprise',contact:'Nom du contact',phone:'Téléphone / WhatsApp',email:'Adresse e-mail',wilaya:'Wilaya',commune:'Commune',product:'Produit souhaité',package:'Conditionnement',quantity:'Quantité souhaitée',message:'Votre message',activity:'Activité commerciale',brands:'Gammes / marques distribuées'}
  },
  ar: {
    title: { quote:'طلب عرض سعر',distributor:'طلب الانضمام إلى شبكة الموزعين' },
    intro: { quote:'اشرح احتياجاتك لإعداد طلب تجاري مستقبلاً.',distributor:'قدّم مؤسستك للانضمام إلى شبكة التوزيع المستقبلية.' },
    disabled:'استمارة توضيحية — الإرسال غير مفعل. لا تُجمع البيانات المدخلة هنا ولا تُرسل.',
    privacy:'يجب اعتماد إجراءات حماية البيانات وربط النظام التجاري قبل تفعيل الاستمارات.',
    consent:'اطلعت على سياسة الخصوصية وأوافق على معالجة طلبي.',
    send:'إرسال الطلب',alternative:'للاتصال بنا حالياً، استخدم البريد الإلكتروني أو واتساب.',
    fields: {business:'اسم المؤسسة',contact:'اسم المسؤول',phone:'الهاتف / واتساب',email:'البريد الإلكتروني',wilaya:'الولاية',commune:'البلدية',product:'المنتج المطلوب',package:'نوع العبوة',quantity:'الكمية المطلوبة',message:'الرسالة',activity:'النشاط التجاري',brands:'المنتجات أو العلامات الموزعة'}
  },
  en: {
    title: { quote:'Request a quotation',distributor:'Distributor application' },
    intro: { quote:'Describe your requirements for a future commercial enquiry.',distributor:'Introduce your company to join our future distribution network.' },
    disabled:'Demonstration form — submission disabled. Information entered here is neither collected nor transmitted.',
    privacy:'Privacy procedures and the CRM integration must be approved before activating forms.',
    consent:'I have read the privacy notice and consent to processing my enquiry.',
    send:'Send enquiry',alternative:'For immediate contact, please use e-mail or WhatsApp.',
    fields: {business:'Company',contact:'Contact name',phone:'Phone / WhatsApp',email:'Email address',wilaya:'Province (wilaya)',commune:'Municipality',product:'Requested product',package:'Packaging',quantity:'Required quantity',message:'Your message',activity:'Business activity',brands:'Products / brands distributed'}
  }
};
