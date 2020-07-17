from django.urls import re_path
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views import *
from django.urls import path



router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
#router.register(r'products', ProductsViewSet, basename='products')
#router.register('staff', StaffViewSet, base_name='staff')
urlpatterns = router.urls
urlpatterns += [
    re_path(r'^products/(?P<pk>[0-9]+)/$', ProductsViewSet.as_view(),
           name='products'),
    #re_path(r'^categories/$', CategoryViewSet.as_view(),
            #name='categories'),
    #re_path(r'^application_references/(?P<reference>\w+)/$', ApplicationReferenceView.as_view(),
    #        name='application_references'),
    #re_path(r'^credit/$', CreditRequestView.as_view(),
    #        name='credits'),
    #re_path(r'^credit/create_api/$', CreditRequestCreateAPIView.as_view(),
    #        name='credits_create_api'),
    #re_path(r'^credit/program/$', ProgramInRequestListView.as_view(),
    #        name='credit_program_list'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/request_to_kib/$', CreditRequestToKibView.as_view(),
    #        name='credit_info_request_to_kib'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/change_status/$', CreditStatusChangeView.as_view(),
    #        name='credit_info_change_status'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/to_verification_stage/$', CreditRequestToVerificationStage.as_view(),
    #        name='to_verification_stage'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/approve/$', CreditRequestApproveView.as_view(),
    #        name='to_approve'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/filling/$', CreditToInWorkView.as_view(),
    #        name='to_filling'),
    #re_path(r'^credit/transfer/$', CreditRequestTransferView.as_view(),
    #        name='transfer'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/against/$', CreditRequestAgainstView.as_view(),
    #        name='against'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/decision/$', CreditRequestDecisionView.as_view(),
    #        name='decision'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/update_cc/$', CreditRequestUpdateCCView.as_view(),
    #        name='update_cc'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/call_back/$', CreditRequestCallBackView.as_view(),
    #        name='to_approve'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/close/$', CreditRequestClose.as_view(),
    #        name='close_credit_request'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/comments/$', CreditRequestCommentsView.as_view(),
    #        name='credit_request_comments'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/business_address/$', CreditRequestBusinessSetAddressView.as_view(),
    #        name='credit_request_comments'),
    #re_path(r'^credit/get_report/$', CreditRequestXlsxView.as_view(),
    #        name='credit_request_comments'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/guarantor/$', GuarantorAddView.as_view(),
    #        name='guarantor_add'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/decisions/$', CreditDecisionListView.as_view(),
    #        name='credit_decisions'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/guarantor_list/$', GuarantorListView.as_view(),
    #        name='close_credit_request'),
    #re_path(r'^credit/guarantor/(?P<pk>[0-9]+)/$', GuarantorInfoView.as_view(),
    #        name='to_approve'),
    #re_path(r'^credit/pledge/(?P<pk>[0-9]+)/$', PledgeInfoView.as_view(),
    #        name='to_approve'),
    #re_path(r'^reports/$', CreditRequestView.as_view(),
    #        name='reports'),
    #re_path(r'^grade-list/$', GradeListView.as_view(),
    #        name='grade-list'),
    #re_path(r'^sms-grade-list/$', GradeSmsListCreateView.as_view(),
    #        name='sms-grade-list'),
    #re_path(r'^sms-grade/(?P<pk>[0-9]+)/$', GradeSmsInfoView.as_view(),
    #        name='sms-grade-list-info'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/program/$', ProgramInRequestView.as_view(),
    #        name='credit_program'),
    #re_path(r'^utils/get_current_date/$', GetCurrentDate.as_view(),
    #        name='get_current_date'),
    #re_path(r'credit/(?P<pk>[0-9]+)/document/consent_to_personal_data/$', consent_to_personal_data_view,
    #        name='consent_to_personal_data'),
    #re_path(r'credit/(?P<pk>[0-9]+)/document/consent_to_kib/$', consent_to_kib_view,
    #        name='consent_to_kib_view'),
    #re_path(r'credit/(?P<pk>[0-9]+)/document/grs_person_doc/$', grs_person_doc_view,
    #        name='grs_person_doc_view'),
    #re_path(r'credit/(?P<pk>[0-9]+)/document/loan_application_print_view/$', loan_application_print_view,
    #        name='loan_application_print_view'),
    #re_path(r'credit/(?P<pk>[0-9]+)/document/decision_doc_view/$', decision_doc_view,
    #        name='decision_doc_view'),
    #re_path(r'credit/(?P<pk>[0-9]+)/document/conclusion_doc_view/$', conclusion_doc_view,
    #        name='conclusion_doc_view'),
    #re_path(r'guarantor/(?P<pk>[0-9]+)/document/guarantor_act_print/$', guarantor_act_print,
    #        name='guarantor_act_print'),
    #re_path(r'pledge/(?P<pk>[0-9]+)/document/pledge_doc_view/$', pledge_doc_view,
    #        name='pledge_doc_view'),
    #re_path(r'sendmail/$', sendmail,
    #        name='sendmail'),
    #re_path(r'putaccess/$', putaccess,
    #        name='putaccess'),
    #re_path(r'sendcompare/$', sendfacecompare,
    #        name='sendcompare'),
    #re_path(r'^credit/(?P<pk>[0-9]+)/program/$', ProgramInRequestView.as_view(),
    #        name='credit_program'),
    # re_path(r'set_pdf_inform/$', set_pdf_inform,
    #        name='set_pdf_inform'),
    # re_path(r'credit/document/get_pdf_report/$', get_pdf_report,
    #        name='get_pdf_report'),
    # re_path(r'send_credit_docs/$', send_credit_docs,
    #        name='send_credit_docs'),
    # re_path(r'get_pdf_request/$', get_pdf_request,
    #        name='get_pdf_request'),
    #  re_path(r'send_to_coll_data/$', send_to_coll_data,
    #        name='send_to_coll_data'),
    #  re_path(r'get_pdf_act/$', get_pdf_act,
    #        name='get_pdf_act'),
    #  re_path(r'send_mrz_detect/$', send_mrz_detect,
    #        name='send_mrz_detect'),
    #  re_path(r'create_request_odb/$', create_request_odb,
    #        name='create_request_odb'),
    #  re_path(r'create_client_odb/$', create_client_odb,
    #        name='create_client_odb'),   
    #  re_path(r'create_contract_odb/$', create_contract_odb,
    #        name='create_contract_odb'),  
    #  re_path(r'get_docx_contract/$', get_docx_contract,
    #        name='get_docx_contract'),        
    #  re_path(r'^credit/get_req_report/$', ReqReportXlsxView.as_view(),
    #        name='request_grs_report'),

    # #Модели для распознования 
    # re_path(r'en/face_landmark_68_model-weights_manifest.json/$', GetModelsJsonAPIView.as_view(),
    #        name='create_model_json'),  
    # re_path(r'en/tiny_face_detector_model-weights_manifest.json/$', GetModelsJsonAPIView.as_view(),
    #        name='create_model_json'), 
    # re_path(r'en/face_recognition_model-weights_manifest.json/$', GetModelsJsonAPIView.as_view(),
    #        name='create_model_json'), 
    # re_path(r'en/face_expression_model-weights_manifest.json/$', GetModelsJsonAPIView.as_view(),
    #        name='create_model_json'), 

    #re_path(r'en/face_expression_model-shard1/$', GetModelsShardAPIView.as_view(),
    #        name='create_model_json'),  
    # re_path(r'en/face_landmark_68_model-shard1/$', GetModelsShardAPIView.as_view(),
    #        name='create_model_json'), 
    # re_path(r'en/tiny_face_detector_model-shard1/$', GetModelsShardAPIView.as_view(),
    #        name='create_model_json'), 
    # re_path(r'en/face_recognition_model-shard1/$', GetModelsShardAPIView.as_view(),
    #        name='create_model_json'), 
    #  re_path(r'en/face_recognition_model-shard2/$', GetModelsShardAPIView.as_view(),
    #        name='create_model_json'),
    #   #re_path(r'services/$', ChatConsumer,
    #   #     name='services'),
    #   re_path(r'faces_recognition/$', faces_recognition,
    #        name='faces_recognition'),
    #   re_path(r'clear_faces/$', clear_faces,
    #        name='clear_faces'),
]
