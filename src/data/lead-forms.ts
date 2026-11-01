import type { Lang } from './site';
export type LeadKind = 'quote' | 'distributor';
export const fieldOrder: Record<LeadKind, readonly string[]> = {
  quote: ['business', 'contact', 'phone', 'email', 'wilaya', 'commune', 'product', 'package', 'quantity', 'message'],
  distributor: ['business', 'contact', 'phone', 'email', 'wilaya', 'commune', 'activity', 'brands', 'message'],
};
export type FieldKey = (typeof fieldOrder)['quote'][number] | (typeof fieldOrder)['distributor'][number];
type Copy = { title: Record<LeadKind,string>; intro:Record<LeadKind,string>; disabled:string; previewTitle:string; previewHelp:string; privacy:string; consent:string; send:string; alternative:string; fields:Record<FieldKey,string> };
export const leadCopy: Record<Lang,Copy> = {
  fr: {
    title: { quote:'Demande de devis',distributor:'Candidature distributeur' },
    intro: { quote:'Aperçu des informations qu’un futur formulaire de devis pourrait demander.',distributor:'Aperçu des informations qu’une future candidature distributeur pourrait demander.' },
    disabled:'Formulaire de démonstration — envoi désactivé. Aucune donnée saisie ici n’est recueillie ni transmise.',
    previewTitle:'Voir les champs de démonstration',previewHelp:'Tous les champs restent désactivés. Aucune saisie ni transmission n’est possible.',
    privacy:'Les formalités de confidentialité et le circuit CRM doivent être validés avant activation des formulaires.',
    consent:'J’ai lu la politique de confidentialité et j’autorise le traitement de cette demande.',
    send:'Envoyer la demande',alternative:'Pour un contact direct, utilisez les coordonnées présentées plus haut.',
    fields: {business:'Entreprise',contact:'Nom du contact',phone:'Téléphone / WhatsApp',email:'Adresse e-mail',wilaya:'Wilaya',commune:'Commune',product:'Produit souhaité',package:'Conditionnement',quantity:'Quantité souhaitée',message:'Votre message',activity:'Activité commerciale',brands:'Gammes / marques distribuées'}
  },
  ar: {
    title: { quote:'طلب عرض سعر',distributor:'طلب الانضمام إلى شبكة الموزعين' },
    intro: { quote:'معاينة المعلومات التي قد تُطلب لاحقًا في استمارة عرض السعر.',distributor:'معاينة المعلومات التي قد تُطلب لاحقًا لطلبات الموزعين.' },
    disabled:'استمارة توضيحية — الإرسال غير مفعل. لا تُجمع البيانات المدخلة هنا ولا تُرسل.',
    previewTitle:'عرض حقول الاستمارة التجريبية',previewHelp:'جميع الحقول معطلة. لا يمكن الإدخال أو الإرسال عبر هذا الموقع.',
    privacy:'يجب اعتماد إجراءات حماية البيانات وربط النظام التجاري قبل تفعيل الاستمارات.',
    consent:'اطلعت على سياسة الخصوصية وأوافق على معالجة طلبي.',
    send:'إرسال الطلب',alternative:'للتواصل المباشر، استخدم وسائل الاتصال الموجودة أعلاه.',
    fields: {business:'اسم المؤسسة',contact:'اسم المسؤول',phone:'الهاتف / واتساب',email:'البريد الإلكتروني',wilaya:'الولاية',commune:'البلدية',product:'المنتج المطلوب',package:'نوع العبوة',quantity:'الكمية المطلوبة',message:'الرسالة',activity:'النشاط التجاري',brands:'المنتجات أو العلامات الموزعة'}
  },
  en: {
    title: { quote:'Request a quotation',distributor:'Distributor application' },
    intro: { quote:'Preview of the information a future quotation form might request.',distributor:'Preview of the information a future distributor application might request.' },
    disabled:'Demonstration form — submission disabled. Information entered here is neither collected nor transmitted.',
    previewTitle:'View demonstration fields',previewHelp:'All fields are disabled. There is no input or submission through this website.',
    privacy:'Privacy procedures and the CRM integration must be approved before activating forms.',
    consent:'I have read the privacy notice and consent to processing my enquiry.',
    send:'Send enquiry',alternative:'For direct contact, use the contact channels shown above.',
    fields: {business:'Company',contact:'Contact name',phone:'Phone / WhatsApp',email:'Email address',wilaya:'Province (wilaya)',commune:'Municipality',product:'Requested product',package:'Packaging',quantity:'Required quantity',message:'Your message',activity:'Business activity',brands:'Products / brands distributed'}
  }
};
