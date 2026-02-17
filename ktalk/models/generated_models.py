"""Auto-generated models from KTalk API specification."""

from datetime import datetime, date
from typing import Dict, Any, List, Optional
from pydantic import BaseModel

class SkbKontur_Talk_Api_Entities_Poll_TalkPoll(BaseModel):
    """Generated model for SkbKontur.Talk.Api.Entities.Poll.TalkPoll."""
    id: Optional[str] = None
    title: Optional[str] = None
    isAnonymous: Optional[bool] = None
    isMultiSelection: Optional[bool] = None
    isRevoteDisabled: Optional[bool] = None
    isCompleted: Optional[bool] = None
    isPublished: Optional[bool] = None
    publishDate: Optional[datetime] = None
    created: Optional[datetime] = None
    createdBy: SkbKontur_Talk_Api_Entities_TalkUserRef
    options: Optional[List[SkbKontur_Talk_Api_Entities_Poll_TalkPollOption]] = None
    votesCount: Optional[int] = None

class SkbKontur_Talk_Api_Entities_Poll_TalkPollOption(BaseModel):
    """Generated model for SkbKontur.Talk.Api.Entities.Poll.TalkPollOption."""
    id: Optional[str] = None
    text: str
    order: Optional[int] = None
    isCorrectAnswer: Optional[bool] = None
    votesCount: Optional[int] = None
    votedUsers: Optional[List[SkbKontur_Talk_Api_Entities_TalkUserRef]] = None
    isChosenByUser: Optional[bool] = None

class SkbKontur_Talk_Api_Entities_TalkUserBaseInfoRef(BaseModel):
    """Generated model for SkbKontur.Talk.Api.Entities.TalkUserBaseInfoRef."""
    anonymousName: Optional[str] = None  # Имя анонима
    anonymousId: Optional[str] = None  # Идентификатор анонима
    userInfo: SkbKontur_Talk_Web_Entities_TalkUserBaseInfo
    isAnonymous: Optional[bool] = None  # Признак анонимного пользователя

class SkbKontur_Talk_Api_Entities_TalkUserRef(BaseModel):
    """Generated model for SkbKontur.Talk.Api.Entities.TalkUserRef."""
    anonymousName: Optional[str] = None  # Имя анонима
    anonymousId: Optional[str] = None  # Идентификатор анонима
    userInfo: SkbKontur_Talk_Web_Entities_TalkUser
    isAnonymous: Optional[bool] = None  # Признак анонимного пользователя

class SkbKontur_Talk_AuditLog_Entities_AuditLogEvent(BaseModel):
    """Generated model for SkbKontur.Talk.AuditLog.Entities.AuditLogEvent."""
    actorId: Optional[str] = None  # Идентификатор актора
    actorType: Optional[str] = None  # Тип актора
    product: Optional[str] = None  # Продукт, к которому относится событие
    eventType: Optional[str] = None  # Тип события
    timestamp: Optional[datetime] = None  # Время действия в UTC
    data: Optional[Dict[str, Any]] = None  # Параметры с дополнительной информацией о действии
    actorIp: Optional[str] = None  # IP актора
    deviceId: Optional[str] = None  # Информация о user-agent, который использовался при выполнении действия
    domainId: Optional[str] = None  # Идентификатор домена
    sessionId: Optional[str] = None  # Хэш токена сессии актора, или токена API-ключа

class SkbKontur_Talk_Calendar_Abstractions_Entities_AttendeeStatus(BaseModel):
    """Generated model for SkbKontur.Talk.Calendar.Abstractions.Entities.AttendeeStatus."""
    pass

class SkbKontur_Talk_Calendar_Abstractions_Entities_AttendeeType(BaseModel):
    """Generated model for SkbKontur.Talk.Calendar.Abstractions.Entities.AttendeeType."""
    pass

class SkbKontur_Talk_Calendar_Abstractions_Entities_CalendarItemBusyType(BaseModel):
    """Generated model for SkbKontur.Talk.Calendar.Abstractions.Entities.CalendarItemBusyType."""
    pass

class SkbKontur_Talk_Common_Data_DeviceTouchSupport(BaseModel):
    """Generated model for SkbKontur.Talk.Common.Data.DeviceTouchSupport."""
    pass

class SkbKontur_Talk_ConferencesHistory_Entities_ConferenceContent(BaseModel):
    """Generated model for SkbKontur.Talk.ConferencesHistory.Entities.ConferenceContent."""
    type: SkbKontur_Talk_ConferencesHistory_Entities_ContentType
    id: Optional[str] = None

class SkbKontur_Talk_ConferencesHistory_Entities_ContentType(BaseModel):
    """Generated model for SkbKontur.Talk.ConferencesHistory.Entities.ContentType."""
    pass

class SkbKontur_Talk_DeepFakeDetector_Api_Enums_TalkDeepFakeDetectionReportFormat(BaseModel):
    """Generated model for SkbKontur.Talk.DeepFakeDetector.Api.Enums.TalkDeepFakeDetectionReportFormat."""
    pass

class SkbKontur_Talk_DeepFakeDetector_Api_Models_TalkConferenceDeepFakeReport(BaseModel):
    """Generated model for SkbKontur.Talk.DeepFakeDetector.Api.Models.TalkConferenceDeepFakeReport."""
    conferenceTitle: Optional[str] = None  # Название встречи
    from_: Optional[datetime] = None  # Время начала встречи
    to: Optional[datetime] = None  # Время окончания встречи
    participants: Optional[List[SkbKontur_Talk_DeepFakeDetector_Api_Models_TalkConferenceDeepFakeReportParticipant]] = None  # Участники встречи
    detections: Optional[List[SkbKontur_Talk_DeepFakeDetector_Api_Models_TalkConferenceDeepFakeReportDetection]] = None  # Результаты детекции дипфейков

class SkbKontur_Talk_DeepFakeDetector_Api_Models_TalkConferenceDeepFakeReportDetection(BaseModel):
    """Generated model for SkbKontur.Talk.DeepFakeDetector.Api.Models.TalkConferenceDeepFakeReportDetection."""
    detectionResult: Optional[str] = None  # Фактический результат: Real - дипфейк не обнаружен, Fake - есть подозрения на дипфейк
    participantId: Optional[str] = None  # Идентификатор участника
    participantName: Optional[str] = None  # Имя участника
    startDetectionTime: Optional[datetime] = None  # Время начала детекции
    endDetectionTime: Optional[datetime] = None  # Время окончания детекции

class SkbKontur_Talk_DeepFakeDetector_Api_Models_TalkConferenceDeepFakeReportParticipant(BaseModel):
    """Generated model for SkbKontur.Talk.DeepFakeDetector.Api.Models.TalkConferenceDeepFakeReportParticipant."""
    participantId: Optional[str] = None  # Идентификатор участника
    participantName: Optional[str] = None  # Имя участника
    participantRole: Optional[str] = None  # Роль участника - задана только для проверяющего

class SkbKontur_Talk_DeepFakeDetector_Api_Models_TalkDeepFakeDetectionDomainStatistics(BaseModel):
    """Generated model for SkbKontur.Talk.DeepFakeDetector.Api.Models.TalkDeepFakeDetectionDomainStatistics."""
    maxDetectionsCount: Optional[int] = None  # Доступное число проверок. Если не ограничено, поле будет пустым
    currentDetectionsCount: Optional[int] = None  # Число уже выполненных проверок на дипфейки

class SkbKontur_Talk_DeepFakeDetector_Api_Models_TalkDeepFakeDetectionStatistic(BaseModel):
    """Generated model for SkbKontur.Talk.DeepFakeDetector.Api.Models.TalkDeepFakeDetectionStatistic."""
    conferences: Optional[int] = None  # Всего конференций в которых проводилась детекция
    tasks: SkbKontur_Talk_DeepFakeDetector_Api_Models_TalkDeepFakeDetectionTasksStatistic

class SkbKontur_Talk_DeepFakeDetector_Api_Models_TalkDeepFakeDetectionTasksByPredictStatistic(BaseModel):
    """Generated model for SkbKontur.Talk.DeepFakeDetector.Api.Models.TalkDeepFakeDetectionTasksByPredictStatistic."""
    real: Optional[int] = None  # Дипфейки не обнаружены - зеленый статус
    fake: Optional[int] = None  # Подозрения на дипфейки - красный статус
    unknown: Optional[int] = None  # Не удалось выявить лица на видео - желтый статус

class SkbKontur_Talk_DeepFakeDetector_Api_Models_TalkDeepFakeDetectionTasksByStateStatistic(BaseModel):
    """Generated model for SkbKontur.Talk.DeepFakeDetector.Api.Models.TalkDeepFakeDetectionTasksByStateStatistic."""
    notFinished: Optional[int] = None  # Начатые, но не завершенные задачи детекции - видео не отправлено на детекцию - желтый статус
    finishedSuccess: Optional[int] = None  # Успешно завершенные задачи детекции - статус в зависимости от результата предсказания
    finishedWithError: Optional[int] = None  # Задачи детекции, завершенные с ошибкой - видео записано, отправлено на детекцию, но не обработано - желтый статус

class SkbKontur_Talk_DeepFakeDetector_Api_Models_TalkDeepFakeDetectionTasksStatistic(BaseModel):
    """Generated model for SkbKontur.Talk.DeepFakeDetector.Api.Models.TalkDeepFakeDetectionTasksStatistic."""
    total: Optional[int] = None  # Всего выполнено задач детекции
    byState: SkbKontur_Talk_DeepFakeDetector_Api_Models_TalkDeepFakeDetectionTasksByStateStatistic
    byPredict: SkbKontur_Talk_DeepFakeDetector_Api_Models_TalkDeepFakeDetectionTasksByPredictStatistic

class SkbKontur_Talk_Kiosk_Api_SearchResult_SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDaemon(BaseModel):
    """Generated model for SkbKontur.Talk.Kiosk.Api.SearchResult_SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskDaemon."""
    items: Optional[List[SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDaemon]] = None
    count: Optional[int] = None  # Количество найденных объектов
    hasMore: Optional[bool] = None  # Признак наличия других объектов

class SkbKontur_Talk_Kiosk_Domain_KioskConferenceStatus(BaseModel):
    """Generated model for SkbKontur.Talk.Kiosk.Domain.KioskConferenceStatus."""
    roomName: Optional[str] = None  # Название комнаты
    streamKey: Optional[str] = None  # Ключ Стрима

class SkbKontur_Talk_Kiosk_Domain_KioskDaemonStatus(BaseModel):
    """Generated model for SkbKontur.Talk.Kiosk.Domain.KioskDaemonStatus."""
    pass

class SkbKontur_Talk_Kiosk_Domain_KioskDeviceCheckStatus(BaseModel):
    """Generated model for SkbKontur.Talk.Kiosk.Domain.KioskDeviceCheckStatus."""
    pass

class SkbKontur_Talk_Kiosk_Domain_KioskEquipmentCheckStatus(BaseModel):
    """Generated model for SkbKontur.Talk.Kiosk.Domain.KioskEquipmentCheckStatus."""
    cameraCheckStatus: SkbKontur_Talk_Kiosk_Domain_KioskDeviceCheckStatus
    microphoneCheckStatus: SkbKontur_Talk_Kiosk_Domain_KioskDeviceCheckStatus
    speakersCheckStatus: SkbKontur_Talk_Kiosk_Domain_KioskDeviceCheckStatus
    lastCheckDate: Optional[datetime] = None  # Дата последней проверки статуса

class SkbKontur_Talk_Kiosk_Domain_KioskMassUpdateAudioSettings(BaseModel):
    """Generated model for SkbKontur.Talk.Kiosk.Domain.KioskMassUpdateAudioSettings."""
    agc: Optional[bool] = None  # Включать автоматическую регулировку громкости микрофона
    ns: Optional[bool] = None  # Включать шумоподавление
    startMuted: Optional[bool] = None  # Подключаться с выключенным микрофоном
    defaultSpeakerVolume: Optional[float] = None  # Громкость звука по умолчанию

class SkbKontur_Talk_Kiosk_Domain_KioskMassUpdateScreensSettings(BaseModel):
    """Generated model for SkbKontur.Talk.Kiosk.Domain.KioskMassUpdateScreensSettings."""
    useSecondScreenForScreenShare: Optional[bool] = None  # Использовать 2 экран для презентаций
    embeddedControllerEnabled: Optional[bool] = None  # Включено ли использование встроенного контроллера (Yealink)

class SkbKontur_Talk_Kiosk_Domain_KioskMassUpdateVideoSettings(BaseModel):
    """Generated model for SkbKontur.Talk.Kiosk.Domain.KioskMassUpdateVideoSettings."""
    wideCamera: Optional[bool] = None  # Использовать широкоформатное видео с камеры
    startMuted: Optional[bool] = None  # Подключаться с выключенной камерой
    sendVideoQuality: Optional[int] = None  # Отправляемое качество видео

class SkbKontur_Talk_Kiosk_Domain_KioskNewsType(BaseModel):
    """Generated model for SkbKontur.Talk.Kiosk.Domain.KioskNewsType."""
    pass

class SkbKontur_Talk_Kiosk_Models_Wallpaper_KioskWallpaperSource(BaseModel):
    """Generated model for SkbKontur.Talk.Kiosk.Models.Wallpaper.KioskWallpaperSource."""
    pass

class SkbKontur_Talk_Kiosk_Statistics_KiosksStatistics(BaseModel):
    """Generated model for SkbKontur.Talk.Kiosk.Statistics.KiosksStatistics."""
    domainId: Optional[str] = None  # Идентификатор домена
    created: Optional[datetime] = None  # Дата статистики
    statistics: Optional[List[SkbKontur_Talk_Kiosk_Statistics_KiosksStatisticsUnit]] = None

class SkbKontur_Talk_Kiosk_Statistics_KiosksStatisticsUnit(BaseModel):
    """Generated model for SkbKontur.Talk.Kiosk.Statistics.KiosksStatisticsUnit."""
    id: Optional[str] = None  # Идентификатор киоска
    title: Optional[str] = None  # Заголовок киоска
    conferencesCount: Optional[int] = None  # Количество конференций, куда подключался киоск
    conferencesMinutes: Optional[int] = None  # Время в минутах, проведенное в конференции

class SkbKontur_Talk_Notes_Api_Enums_TalkNoteLinkTargetType(BaseModel):
    """Generated model for SkbKontur.Talk.Notes.Api.Enums.TalkNoteLinkTargetType."""
    pass

class SkbKontur_Talk_Notes_Api_Models_TalkNoteInfo(BaseModel):
    """Generated model for SkbKontur.Talk.Notes.Api.Models.TalkNoteInfo."""
    key: str
    title: str
    createdBy: SkbKontur_Talk_Web_Entities_TalkUser
    createdDate: datetime
    modifiedBy: SkbKontur_Talk_Web_Entities_TalkUser
    modifiedDate: Optional[datetime] = None
    participantsAccessEnabled: Optional[bool] = None
    latestLink: SkbKontur_Talk_Notes_Api_Models_TalkNoteLink

class SkbKontur_Talk_Notes_Api_Models_TalkNoteLink(BaseModel):
    """Generated model for SkbKontur.Talk.Notes.Api.Models.TalkNoteLink."""
    targetType: SkbKontur_Talk_Notes_Api_Enums_TalkNoteLinkTargetType
    targetKey: Optional[str] = None  # Ключ связи
    createdDate: Optional[datetime] = None  # Дата создания
    title: Optional[str] = None  # Название
    metaInfo: Optional[Dict[str, Any]] = None  # Метаинформация

class SkbKontur_Talk_Platform_UserDomains_Configuration_Calendar_CalDavServerType(BaseModel):
    """Generated model for SkbKontur.Talk.Platform.UserDomains.Configuration.Calendar.CalDavServerType."""
    pass

class SkbKontur_Talk_Platform_UserDomains_Configuration_Calendar_EwsVersion(BaseModel):
    """Generated model for SkbKontur.Talk.Platform.UserDomains.Configuration.Calendar.EwsVersion."""
    pass

class SkbKontur_Talk_Platform_Users_Domain_UserGeoInfo(BaseModel):
    """Generated model for SkbKontur.Talk.Platform.Users.Domain.UserGeoInfo."""
    ip: Optional[str] = None
    region: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None

class SkbKontur_Talk_Recordings_Domain_RecordingsOrderMode(BaseModel):
    """Generated model for SkbKontur.Talk.Recordings.Domain.RecordingsOrderMode."""
    pass

class SkbKontur_Talk_Recordings_Domain_VideoMediaUploadStatus(BaseModel):
    """Generated model for SkbKontur.Talk.Recordings.Domain.VideoMediaUploadStatus."""
    pass

class SkbKontur_Talk_Resources_Access_LinkAccess_ResourceLinkAccessScope(BaseModel):
    """Generated model for SkbKontur.Talk.Resources.Access.LinkAccess.ResourceLinkAccessScope."""
    pass

class SkbKontur_Talk_Rooms_Statistics_Reports_Models_ParticipantTotalDurationModel(BaseModel):
    """Generated model for SkbKontur.Talk.Rooms.Statistics.Reports.Models.ParticipantTotalDurationModel."""
    participantName: Optional[str] = None  # Имя участника
    isGuest: Optional[bool] = None  # Признак является ли участник гостем
    participant: Optional[str] = None  # Статус участника (Гость/ Участник)
    participantEmail: Optional[str] = None  # Email
    sessionHall: Optional[str] = None  # Сессионный зал
    duration: Optional[str] = None  # Общая продолжительность нахождения в комнате в формате hh:mm:ss

class SkbKontur_Talk_Rooms_Statistics_Reports_Models_RoomStatisticsParticipantModel(BaseModel):
    """Generated model for SkbKontur.Talk.Rooms.Statistics.Reports.Models.RoomStatisticsParticipantModel."""
    participantName: Optional[str] = None  # Имя участника
    participantId: Optional[str] = None  # Id участника
    isGuest: Optional[bool] = None  # Признак является ли участник гостем
    participant: Optional[str] = None  # Статус участника (Гость/ Участник)
    participantEmail: Optional[str] = None  # Email
    sessionHall: Optional[str] = None  # Сессионный зал
    entryTime: Optional[datetime] = None  # Дата и время входа в конференцию
    exitTime: Optional[datetime] = None  # Дата и время выхода из конференции
    urlParams: Optional[str] = None  # Параметры URL из ссылки, по которой присоединился участник

class SkbKontur_Talk_Rooms_Statistics_Reports_Models_RoomStatisticsReportMetricsModel(BaseModel):
    """Generated model for SkbKontur.Talk.Rooms.Statistics.Reports.Models.RoomStatisticsReportMetricsModel."""
    streamViewersCount: Optional[int] = None
    streamViewersBuildSecondsDuration: Optional[int] = None

class SkbKontur_Talk_Rooms_Statistics_Reports_Models_Stream_StreamStatisticsViewerModel(BaseModel):
    """Generated model for SkbKontur.Talk.Rooms.Statistics.Reports.Models.Stream.StreamStatisticsViewerModel."""
    viewerKey: Optional[str] = None
    viewerName: Optional[str] = None
    viewerEmail: Optional[str] = None
    isGuest: Optional[bool] = None
    viewer: Optional[str] = None
    entryTime: Optional[datetime] = None
    exitTime: Optional[datetime] = None
    duration: Optional[str] = None
    geoInfo: SkbKontur_Talk_Platform_Users_Domain_UserGeoInfo

class SkbKontur_Talk_SpeechCore_Api_Models_Summarization_TalkSummary(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Summarization.TalkSummary."""
    summaryId: Optional[str] = None  # Уникальный идентификатор резюме встречи
    chunks: Optional[List[SkbKontur_Talk_SpeechCore_Api_Models_Summarization_TalkSummaryChunk]] = None  # Отдельные части резюме встречи с указанием временных меток
    hidden: Optional[bool] = None  # Признак скрытия резюме встречи в интерфейсе пользователя
    hiddenReason: Optional[str] = None  # Причина скрытия резюме встречи
    hiddenBy: SkbKontur_Talk_Web_Entities_TalkUser
    hiddenAt: Optional[datetime] = None  # Дата и время скрытия резюме встречи

class SkbKontur_Talk_SpeechCore_Api_Models_Summarization_TalkSummaryChunk(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Summarization.TalkSummaryChunk."""
    id: Optional[str] = None  # Идентификатор части
    text: Optional[str] = None  # Текст
    timestamp: Optional[int] = None  # Временная метка в секундах

class SkbKontur_Talk_SpeechCore_Api_Models_Summarization_TalkSummaryHiddenStatus(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Summarization.TalkSummaryHiddenStatus."""
    isHidden: Optional[bool] = None  # Признак скрытия суммаризации встречи в интерфейсе пользователя
    hiddenReason: Optional[str] = None  # Причина скрытия
    hiddenBy: SkbKontur_Talk_Web_Entities_TalkUser
    hiddenAt: Optional[datetime] = None  # Дата и время скрытия

class SkbKontur_Talk_SpeechCore_Api_Models_Summarization_TalkSummaryResult(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Summarization.TalkSummaryResult."""
    status: SkbKontur_Talk_SpeechCore_Api_Models_Summarization_TalkSummaryStatus
    summary: SkbKontur_Talk_SpeechCore_Api_Models_Summarization_TalkSummary

class SkbKontur_Talk_SpeechCore_Api_Models_Summarization_TalkSummaryStatus(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Summarization.TalkSummaryStatus."""
    pass

class SkbKontur_Talk_SpeechCore_Api_Models_Summarization_TalkSummaryType(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Summarization.TalkSummaryType."""
    pass

class SkbKontur_Talk_SpeechCore_Api_Models_Summarization_TalkSummaryV2Chunk(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Summarization.TalkSummaryV2Chunk."""
    type: Optional[str] = None  # Тип
    timestamp: Optional[int] = None  # Временная метка
    version: Optional[int] = None  # Версия
    text: Optional[str] = None  # Текст
    hiddenStatus: SkbKontur_Talk_SpeechCore_Api_Models_Summarization_TalkSummaryHiddenStatus

class SkbKontur_Talk_SpeechCore_Api_Models_Summarization_TalkSummaryV2Result(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Summarization.TalkSummaryV2Result."""
    summaryId: Optional[str] = None  # Уникальный идентификатор
    status: SkbKontur_Talk_SpeechCore_Api_Models_TalkSpeechCoreResultStatus
    chunks: Optional[List[SkbKontur_Talk_SpeechCore_Api_Models_Summarization_TalkSummaryV2Chunk]] = None  # Отдельные части суммаризации встречи с указанием временных меток
    hidden: Optional[bool] = None  # Признак скрытия в интерфейсе пользователя
    hiddenReason: Optional[str] = None  # Причина скрытия
    hiddenBy: SkbKontur_Talk_Web_Entities_TalkUser
    hiddenAt: Optional[datetime] = None  # Дата и время скрытия

class SkbKontur_Talk_SpeechCore_Api_Models_TalkCompositeSpeechCoreResult(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.TalkCompositeSpeechCoreResult."""
    transcriptionV2: SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscriptionV2Result
    shortSummaryV2: SkbKontur_Talk_SpeechCore_Api_Models_Summarization_TalkSummaryV2Result
    protocolV2: SkbKontur_Talk_SpeechCore_Api_Models_Summarization_TalkSummaryV2Result

class SkbKontur_Talk_SpeechCore_Api_Models_TalkSpeechCoreResultStatus(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.TalkSpeechCoreResultStatus."""
    pass

class SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscript(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Transcription.TalkTranscript."""
    status: SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscriptionStatus
    statusMessage: Optional[str] = None  # Сообщение о статусе
    tracks: Optional[List[SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscriptTrack]] = None
    errors: Optional[List[SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscriptionError]] = None

class SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscriptChunk(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Transcription.TalkTranscriptChunk."""
    timeOffsetInMillis: Optional[int] = None
    startTimeOffsetInMillis: Optional[int] = None
    endTimeOffsetInMillis: Optional[int] = None
    text: Optional[str] = None
    words: Optional[List[SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscriptWord]] = None
    confidence: Optional[float] = None

class SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscriptTrack(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Transcription.TalkTranscriptTrack."""
    speaker: SkbKontur_Talk_Api_Entities_TalkUserRef
    dearizedSpeaker: SkbKontur_Talk_Api_Entities_TalkUserRef
    chunks: Optional[List[SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscriptChunk]] = None
    confidence: Optional[float] = None

class SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscriptWord(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Transcription.TalkTranscriptWord."""
    startTimeOffsetInMillis: Optional[int] = None
    endTimeOffsetInMillis: Optional[int] = None
    text: Optional[str] = None
    confidence: Optional[float] = None

class SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscription(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Transcription.TalkTranscription."""
    transcriptionUrl: Optional[str] = None
    status: SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscriptionStatus

class SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscriptionError(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Transcription.TalkTranscriptionError."""
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    message: Optional[str] = None

class SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscriptionStatus(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Transcription.TalkTranscriptionStatus."""
    pass

class SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscriptionV2Result(BaseModel):
    """Generated model for SkbKontur.Talk.SpeechCore.Api.Models.Transcription.TalkTranscriptionV2Result."""
    status: SkbKontur_Talk_SpeechCore_Api_Models_TalkSpeechCoreResultStatus
    statusMessage: Optional[str] = None  # Сообщение о статусе
    tracks: Optional[List[SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscriptTrack]] = None
    errors: Optional[List[SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscriptionError]] = None

class SkbKontur_Talk_Web_Entities_Access_PatchUsersAccessRequest(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Access.PatchUsersAccessRequest."""
    userKey: str  # Идентификатор пользователя
    roleId: str  # Идентификатор роли

class SkbKontur_Talk_Web_Entities_Access_UsersAccessResponse(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Access.UsersAccessResponse."""
    user: SkbKontur_Talk_Web_Entities_TalkUser
    roleId: str  # Идентификатор роли

class SkbKontur_Talk_Web_Entities_Calendar_CalendarServerCreateModel(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.CalendarServerCreateModel."""
    title: str  # Название календаря
    integrationSettings: SkbKontur_Talk_Web_Entities_Features_TalkCalendarFeatureSettingsModify
    domainRules: List[str]  # Список доменов, к которым применяется календарь

class SkbKontur_Talk_Web_Entities_Calendar_CalendarServerResponseModel(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.CalendarServerResponseModel."""
    calendarServerId: Optional[str] = None  # Идентификатор настроек календаря
    title: Optional[str] = None  # Название календаря
    type: SkbKontur_Talk_Web_Entities_Calendar_TalkCalendarType
    integrationSettings: SkbKontur_Talk_Web_Entities_Features_TalkCalendarFeatureSettingsModify
    domainRules: Optional[List[str]] = None  # Список доменов к которым применяется данный календарь

class SkbKontur_Talk_Web_Entities_Calendar_CalendarServerShortResponseModel(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.CalendarServerShortResponseModel."""
    calendarSettingsId: Optional[str] = None  # Идентификатор настроек дополнительного календаря
    title: Optional[str] = None  # Название дополнительного календаря
    type: SkbKontur_Talk_Web_Entities_Calendar_TalkCalendarType

class SkbKontur_Talk_Web_Entities_Calendar_CalendarServerUpdateModel(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.CalendarServerUpdateModel."""
    title: str  # Название календаря
    integrationSettings: SkbKontur_Talk_Web_Entities_Features_TalkCalendarFeatureSettingsModify
    domainRules: List[str]  # Список доменов, к которым применяется календарь

class SkbKontur_Talk_Web_Entities_Calendar_CreateEmailCalendarEventModel(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.CreateEmailCalendarEventModel."""
    start: Optional[datetime] = None  # Дата начала встречи
    end: Optional[datetime] = None  # Дата окончания встречи
    timezone: Optional[str] = None  # Временная зона в формате GMT+X
    subject: str  # Тема встречи
    description: Optional[str] = None  # Описание встречи
    roomName: str  # Комната в которой будет проходить встреча
    allowAnonymous: Optional[bool] = None  # Разрешить присутствие внешних пользователей
    enableSip: Optional[bool] = None  # Включить возможность позвонить в конференцию по протоколу SIP
    pinCode: Optional[str] = None  # Устанавливает пин код для комнаты
    enableAutoRecording: Optional[bool] = None  # Включить автоматическую запись встречи
    isRecurring: Optional[bool] = None  # Признак, что встреча является повторяющейся
    recurrence: SkbKontur_Talk_Web_Entities_Calendar_Recurrence_TalkCalendarRecurrence
    simultaneousTranslation: SkbKontur_Talk_Web_Entities_Rooms_TalkSimultaneousTranslationUpdateRequest
    customMeetingUrl: Optional[str] = None  # Пользовательский URL
    maskingSettings: SkbKontur_Talk_Web_Entities_Rooms_Masking_TalkMaskingSettings
    autoRunDeepFakeDetection: Optional[bool] = None  # Настройка автоматического запуска детекции дипфейков в комнате
    isAllDayEvent: Optional[bool] = None  # Регулярная встреча
    requiredUserKeys: List[str]  # Список обязательных участников встречи
    optionalUserKeys: Optional[List[str]] = None  # Список не обязательных участников встречи
    requiredExternalAttendeesEmails: Optional[List[str]] = None  # Список обязательных внешних участников
    optionExternalAttendeesEmails: Optional[List[str]] = None  # Список не обязательных внешних участников
    controlledViaExternalSystem: Optional[bool] = None  # Встреча управляется внешней системой

class SkbKontur_Talk_Web_Entities_Calendar_EditEmailCalendarAttendeeModel(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.EditEmailCalendarAttendeeModel."""
    requiredUserKeys: Optional[List[str]] = None  # Список обязательных участников встречи
    optionalUserKeys: Optional[List[str]] = None  # Список не обязательных участников встречи
    requiredExternalAttendeesEmails: Optional[List[str]] = None  # Список обязательных внешних участников
    optionExternalAttendeesEmails: Optional[List[str]] = None  # Список не обязательных внешних участников

class SkbKontur_Talk_Web_Entities_Calendar_EditEmailCalendarEventModel(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.EditEmailCalendarEventModel."""
    start: Optional[datetime] = None  # Дата начала встречи
    end: Optional[datetime] = None  # Дата окончания встречи
    timezone: Optional[str] = None  # Временная зона в формате GMT+X
    subject: str  # Тема встречи
    description: Optional[str] = None  # Описание встречи
    roomName: str  # Комната в которой будет проходить встреча
    allowAnonymous: Optional[bool] = None  # Разрешить присутствие внешних пользователей
    enableSip: Optional[bool] = None  # Включить возможность позвонить в конференцию по протоколу SIP
    pinCode: Optional[str] = None  # Устанавливает пин код для комнаты
    enableAutoRecording: Optional[bool] = None  # Включить автоматическую запись встречи
    isRecurring: Optional[bool] = None  # Признак, что встреча является повторяющейся
    recurrence: SkbKontur_Talk_Web_Entities_Calendar_Recurrence_TalkCalendarRecurrence
    simultaneousTranslation: SkbKontur_Talk_Web_Entities_Rooms_TalkSimultaneousTranslationUpdateRequest
    customMeetingUrl: Optional[str] = None  # Пользовательский URL
    maskingSettings: SkbKontur_Talk_Web_Entities_Rooms_Masking_TalkMaskingSettings
    autoRunDeepFakeDetection: Optional[bool] = None  # Настройка автоматического запуска детекции дипфейков в комнате

class SkbKontur_Talk_Web_Entities_Calendar_EmailCalendarItem(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.EmailCalendarItem."""
    calendarSource: Optional[str] = None  # Календарь, из которого создан ряд встреч
    busyType: SkbKontur_Talk_Calendar_Abstractions_Entities_CalendarItemBusyType
    subject: Optional[str] = None  # Название встречи
    description: Optional[str] = None  # Описание
    start: Optional[datetime] = None  # Дата и время начала
    end: Optional[datetime] = None  # Дата и время окончания
    location: Optional[str] = None  # Место проведения
    organizer: SkbKontur_Talk_Web_Entities_Calendar_EmailCalendarItemAttendee
    requiredAttendees: Optional[List[SkbKontur_Talk_Web_Entities_Calendar_EmailCalendarItemAttendee]] = None  # Обязательные участники
    optionalAttendees: Optional[List[SkbKontur_Talk_Web_Entities_Calendar_EmailCalendarItemAttendee]] = None  # Необязательные участники
    isAllDayEvent: Optional[bool] = None  # Событие на весь день
    isCancelled: Optional[bool] = None  # Признак отмененного мероприятия
    enableAutoRecording: Optional[bool] = None  # Включена автозапись встречи
    onlineUsersCount: Optional[int] = None  # Количество пользователей онлайн
    onlineUsers: Optional[List[SkbKontur_Talk_Api_Entities_TalkUserRef]] = None  # Информация о пользователях
    roomName: Optional[str] = None  # Комната в которой будет проходить встреча
    stream: SkbKontur_Talk_Web_Entities_Rooms_TalkRoomStream
    room: SkbKontur_Talk_Web_Entities_Rooms_TalkRoom
    onlineMeetingUrl: Optional[str] = None  # Ссылка на встречу
    externalMeeting: SkbKontur_Talk_Web_Entities_Calendar_TalkExternalMeeting
    id: Optional[str] = None  # Идентификатор мероприятия в календаре
    isRecurring: Optional[bool] = None  # Признак повторяющейся встречи
    recurrence: SkbKontur_Talk_Web_Entities_Calendar_Recurrence_TalkCalendarRecurrence
    isPrivate: Optional[bool] = None  # Признак приватной встречи

class SkbKontur_Talk_Web_Entities_Calendar_EmailCalendarItemAttendee(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.EmailCalendarItemAttendee."""
    user: SkbKontur_Talk_Web_Entities_TalkUser
    name: Optional[str] = None  # Имя пользователя
    mailbox: Optional[str] = None  # Email пользователя
    type: SkbKontur_Talk_Calendar_Abstractions_Entities_AttendeeType
    status: SkbKontur_Talk_Calendar_Abstractions_Entities_AttendeeStatus

class SkbKontur_Talk_Web_Entities_Calendar_EmailCalendarResult(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.EmailCalendarResult."""
    items: Optional[List[SkbKontur_Talk_Web_Entities_Calendar_EmailCalendarItem]] = None  # Список встреч

class SkbKontur_Talk_Web_Entities_Calendar_ExternalMeetingType(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.ExternalMeetingType."""
    pass

class SkbKontur_Talk_Web_Entities_Calendar_Recurrence_TalkCalendarDayOfTheWeek(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.Recurrence.TalkCalendarDayOfTheWeek."""
    pass

class SkbKontur_Talk_Web_Entities_Calendar_Recurrence_TalkCalendarDayOfTheWeekIndex(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.Recurrence.TalkCalendarDayOfTheWeekIndex."""
    pass

class SkbKontur_Talk_Web_Entities_Calendar_Recurrence_TalkCalendarMonth(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.Recurrence.TalkCalendarMonth."""
    pass

class SkbKontur_Talk_Web_Entities_Calendar_Recurrence_TalkCalendarRecurrence(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.Recurrence.TalkCalendarRecurrence."""
    type: SkbKontur_Talk_Web_Entities_Calendar_Recurrence_TalkCalendarRecurrencePatternType
    startDate: Optional[datetime] = None  # Дата начала
    endDate: Optional[datetime] = None  # Дата окончания
    numberOfEvents: Optional[int] = None  # Количество встреч в ряде
    interval: Optional[int] = None  # Интервал повторений
    dayOfMonth: Optional[int] = None  # День месяца в который будут проходить встречи
    daysOfTheWeek: Optional[List[SkbKontur_Talk_Web_Entities_Calendar_Recurrence_TalkCalendarDayOfTheWeek]] = None  # Дни недели, в которые будут проходить встречи
    month: SkbKontur_Talk_Web_Entities_Calendar_Recurrence_TalkCalendarMonth
    dayOfTheWeekIndex: SkbKontur_Talk_Web_Entities_Calendar_Recurrence_TalkCalendarDayOfTheWeekIndex
    firstEventId: Optional[str] = None  # Идентификатор первой встречи ряда

class SkbKontur_Talk_Web_Entities_Calendar_Recurrence_TalkCalendarRecurrencePatternType(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.Recurrence.TalkCalendarRecurrencePatternType."""
    pass

class SkbKontur_Talk_Web_Entities_Calendar_TalkCalendarType(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.TalkCalendarType."""
    pass

class SkbKontur_Talk_Web_Entities_Calendar_TalkExternalMeeting(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calendar.TalkExternalMeeting."""
    url: Optional[str] = None  # Адрес
    type: SkbKontur_Talk_Web_Entities_Calendar_ExternalMeetingType

class SkbKontur_Talk_Web_Entities_Calls_TalkCallee(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calls.TalkCallee."""
    userKey: Optional[str] = None  # Ключ пользователя
    userCallMethod: SkbKontur_Talk_Web_Entities_Calls_TalkUserCallMethod
    phoneNumber: Optional[str] = None  # Номер телефона, если не указан UserKey
    email: Optional[str] = None  # Почта, если не указан UserKey
    talkSipCallId: Optional[str] = None  # Идентификатор вызываемого SIP-а
    user: SkbKontur_Talk_Web_Entities_TalkUser

class SkbKontur_Talk_Web_Entities_Calls_TalkCalleeRequest(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calls.TalkCalleeRequest."""
    userKey: Optional[str] = None  # Ключ пользователя
    userCallMethod: SkbKontur_Talk_Web_Entities_Calls_TalkUserCallMethod
    phoneNumber: Optional[str] = None  # Номер телефона, если не указан UserKey
    email: Optional[str] = None  # Почта, если не указан UserKey
    talkSipCallId: Optional[str] = None  # Идентификатор вызываемого SIP-а

class SkbKontur_Talk_Web_Entities_Calls_TalkCancelCallParameters(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calls.TalkCancelCallParameters."""
    callees: Optional[List[SkbKontur_Talk_Web_Entities_Calls_TalkCalleeRequest]] = None  # Пользователи для которых нужно отменить звонок. Если не указаны, то отменяется для всех
    callerUserKey: Optional[str] = None  # Пользователь, от лица которого совершается звонок, если вызов идет с API-ключом

class SkbKontur_Talk_Web_Entities_Calls_TalkNotifyCallParameters(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calls.TalkNotifyCallParameters."""
    callees: List[SkbKontur_Talk_Web_Entities_Calls_TalkCalleeRequest]  # Вызываемые пользователи
    roomTitle: Optional[str] = None  # Заголовок комнаты
    callerUserKey: Optional[str] = None  # Пользователь, от лица которого совершается звонок, если вызов идет с API-ключом

class SkbKontur_Talk_Web_Entities_Calls_TalkNotifyCallResult(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calls.TalkNotifyCallResult."""
    calleeResults: Optional[List[SkbKontur_Talk_Web_Entities_Calls_TalkNotifyCalleeResult]] = None

class SkbKontur_Talk_Web_Entities_Calls_TalkNotifyCalleeResult(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calls.TalkNotifyCalleeResult."""
    callee: SkbKontur_Talk_Web_Entities_Calls_TalkCallee
    status: SkbKontur_Talk_Web_Entities_Calls_TalkNotifyCalleeStatus
    statusMessage: Optional[str] = None

class SkbKontur_Talk_Web_Entities_Calls_TalkNotifyCalleeStatus(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calls.TalkNotifyCalleeStatus."""
    pass

class SkbKontur_Talk_Web_Entities_Calls_TalkUserCallMethod(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Calls.TalkUserCallMethod."""
    pass

class SkbKontur_Talk_Web_Entities_ClientsTelemetry_ClientsTelemetryInfo(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.ClientsTelemetry.ClientsTelemetryInfo."""
    timestamp: Optional[datetime] = None  # Метка времени телеметрии
    name: str  # Тип телеметрии
    data: List[Any]  # Набор произвольных данных телеметрии, содержащих ключи и значения

Возможные поля:
- actor.key: Ключ пользователя. только для авторизованных пользователей
- actor.email: Почта пользователя. только для авторизованных пользователей
- actor.name: Имя пользователя/Анонимного пользователя
- actor.type: Тип пользователя: Anonymous/User
- room.name: Название комнаты
- platform: Платформа пользователя: Web/Electron
- app.platform: Используемое пользователем приложение
- latency.min/latency.max/latency.avg (int): Задержка сети
- jitter.min/jitter.max/jitter.avg (int): Интервалы потока для аудио и видео
- packet.loss.download.min/packet.loss.download.max/packet.loss.download.avg (int): Потери пакетов на загрузку
- packet.loss.upload.min/packet.loss.upload.max/packet.loss.upload.avg (int): Потери пакетов на передачу
- bwe.download.min/bwe.download.max/bwe.download.avg (int): Оценка пропускной способности сети на загрузку
- bwe.upload.min/bwe.upload.max/bwe.upload.avg (int): Оценка пропускной способности сети на передачу
- bitrate.download.min/bitrate.download.max/bitrate.download.avg (int): Скорость загрузки данных
- bitrate.upload.min/bitrate.upload.max/bitrate.upload.avg (int): Скорость передачи данных


class SkbKontur_Talk_Web_Entities_ClientsTelemetry_ClientsTelemetryInfoV2(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.ClientsTelemetry.ClientsTelemetryInfoV2."""
    timestamp: Optional[datetime] = None  # Метка времени телеметрии
    name: str  # Тип телеметрии
    data: List[Any]  # Набор произвольных данных телеметрии, содержащих ключи и значения

class SkbKontur_Talk_Web_Entities_ClientsTelemetry_ClientsTelemetryItem_System_Boolean(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.ClientsTelemetry.ClientsTelemetryItem_System.Boolean."""
    key: Optional[str] = None  # Название элемента телеметрии
    value: Optional[bool] = None  # Значение

class SkbKontur_Talk_Web_Entities_ClientsTelemetry_ClientsTelemetryItem_System_Int32(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.ClientsTelemetry.ClientsTelemetryItem_System.Int32."""
    key: Optional[str] = None  # Название элемента телеметрии
    value: Optional[int] = None  # Значение

class SkbKontur_Talk_Web_Entities_ClientsTelemetry_ClientsTelemetryItem_System_Single(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.ClientsTelemetry.ClientsTelemetryItem_System.Single."""
    key: Optional[str] = None  # Название элемента телеметрии
    value: Optional[float] = None  # Значение

class SkbKontur_Talk_Web_Entities_ClientsTelemetry_ClientsTelemetryItem_System_String(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.ClientsTelemetry.ClientsTelemetryItem_System.String."""
    key: Optional[str] = None  # Название элемента телеметрии
    value: Optional[str] = None  # Значение

class SkbKontur_Talk_Web_Entities_ClientsTelemetry_ClientsTelemetryResponse(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.ClientsTelemetry.ClientsTelemetryResponse."""
    telemetry: List[SkbKontur_Talk_Web_Entities_ClientsTelemetry_ClientsTelemetryInfo]  # Массив объектов телеметрии клиентов
    nextPageToken: Optional[str] = None  # Токен для получения следующей страницы данных, если она существует

class SkbKontur_Talk_Web_Entities_ClientsTelemetry_ClientsTelemetryResponseV2(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.ClientsTelemetry.ClientsTelemetryResponseV2."""
    telemetry: List[SkbKontur_Talk_Web_Entities_ClientsTelemetry_ClientsTelemetryInfoV2]  # Массив объектов телеметрии клиентов
    nextPageToken: Optional[str] = None  # Токен для получения следующей страницы данных, если она существует

class SkbKontur_Talk_Web_Entities_Conferences_Report_TalkConferenceActivityReport(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Conferences.Report.TalkConferenceActivityReport."""
    totalParticipantsCount: Optional[int] = None  # Общее количество участников встречи
    pageParticipantsCount: Optional[int] = None  # Количество участников встречи в ответе
    conferenceStartTime: Optional[datetime] = None  # Время начала встречи по UTC
    conferenceEndTime: Optional[datetime] = None  # Время окончания встречи по UTC
    pollsCount: Optional[int] = None  # Общее количество голосований, опубликованных на встрече
    messagesCount: Optional[int] = None  # Общее количество сообщений в канале "общие" на встрече
    questionsCount: Optional[int] = None  # Общее количество сообщений в канале "вопросы" на встрече
    participantsActivities: Optional[List[SkbKontur_Talk_Web_Entities_Conferences_Report_TalkParticipantActivityReport]] = None  # Массив метрик активности участников

class SkbKontur_Talk_Web_Entities_Conferences_Report_TalkConferenceChatReport(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Conferences.Report.TalkConferenceChatReport."""
    messages: Optional[List[SkbKontur_Talk_Web_Entities_Conferences_Report_TalkConferenceChatReportMessage]] = None

class SkbKontur_Talk_Web_Entities_Conferences_Report_TalkConferenceChatReportAttachment(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Conferences.Report.TalkConferenceChatReportAttachment."""
    downloadUrl: Optional[str] = None  # Ссылка
    fileName: Optional[str] = None  # Название файла
    fileId: Optional[str] = None  # Идентификатор поля

class SkbKontur_Talk_Web_Entities_Conferences_Report_TalkConferenceChatReportMessage(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Conferences.Report.TalkConferenceChatReportMessage."""
    created: Optional[datetime] = None  # Дата создания
    sender: SkbKontur_Talk_Web_Entities_Conferences_Report_TalkConferenceReportParticipant
    recipient: SkbKontur_Talk_Web_Entities_Conferences_Report_TalkConferenceReportParticipant
    isPrivate: Optional[bool] = None  # Признак приватного сообщения
    text: Optional[str] = None  # Содержимое
    attachments: Optional[List[SkbKontur_Talk_Web_Entities_Conferences_Report_TalkConferenceChatReportAttachment]] = None  # Приложения

class SkbKontur_Talk_Web_Entities_Conferences_Report_TalkConferenceParticipantsReport(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Conferences.Report.TalkConferenceParticipantsReport."""
    participants: Optional[List[SkbKontur_Talk_Web_Entities_Conferences_Report_TalkConferenceReportParticipantExtendedInfo]] = None

class SkbKontur_Talk_Web_Entities_Conferences_Report_TalkConferenceReportParticipant(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Conferences.Report.TalkConferenceReportParticipant."""
    participantId: Optional[str] = None  # Идентификатор участника
    participantName: Optional[str] = None  # Имя участника
    isGuest: Optional[bool] = None  # Является ли участник гостем

class SkbKontur_Talk_Web_Entities_Conferences_Report_TalkConferenceReportParticipantConnectionInfo(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Conferences.Report.TalkConferenceReportParticipantConnectionInfo."""
    appPlatform: Optional[str] = None
    isViaProxy: Optional[bool] = None
    participantRealIp: Optional[str] = None
    country: Optional[str] = None

class SkbKontur_Talk_Web_Entities_Conferences_Report_TalkConferenceReportParticipantExtendedInfo(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Conferences.Report.TalkConferenceReportParticipantExtendedInfo."""
    participantId: Optional[str] = None  # Идентификатор участника
    participantName: Optional[str] = None  # Имя участника
    isGuest: Optional[bool] = None  # Является ли участник гостем
    connectionsInfo: Optional[List[SkbKontur_Talk_Web_Entities_Conferences_Report_TalkConferenceReportParticipantConnectionInfo]] = None

class SkbKontur_Talk_Web_Entities_Conferences_Report_TalkParticipantActivityReport(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Conferences.Report.TalkParticipantActivityReport."""
    participantId: Optional[str] = None  # Уникальный идентификатор участника.
Значение равно UserKey для зарегестрированного пользователя и AnonymousId для внешнего пользователя
    participantName: Optional[str] = None  # Имя участника
    email: Optional[str] = None  # Электронный адрес участника. Только для зарегистрированных пользователей
    isGuest: Optional[bool] = None  # Является ли пользователь внешним участником
    pollsCount: Optional[int] = None  # Количество опросов, опубликованных участником
    pollVotesCount: Optional[int] = None  # Количество голосов участника в опросах
    messagesCount: Optional[int] = None  # Количество сообщений участника в канале "Общие"
    questionsCount: Optional[int] = None  # Количество сообщений участника в канале "Вопросы"
    raiseHandCount: Optional[int] = None  # Сколько раз участник поднимал руку
    duration: Optional[str] = None  # Сколько времени участник провел на встрече
    speechDuration: Optional[str] = None  # Сколько времени у участника был включен микрофон
    cameraDuration: Optional[str] = None  # Сколько времени у участника была включена камера
    screenShareDuration: Optional[str] = None  # Сколько времени участник демонстрировал экран

class SkbKontur_Talk_Web_Entities_Conferences_TalkConference(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Conferences.TalkConference."""
    key: Optional[str] = None  # Ключ конференции
    roomName: Optional[str] = None  # Название комнаты
    startTime: Optional[datetime] = None  # Дата начала конференции
    endTime: Optional[datetime] = None  # Дата окончания конференции
    title: Optional[str] = None  # Заголовок
    isPlannedMeeting: Optional[bool] = None  # Была ли конференция запланированной
    containsDeepFakeDetections: Optional[bool] = None  # Признак конференции, проверенной на наличие дипфейков
    description: Optional[str] = None  # Описание
    artifacts: SkbKontur_Talk_Web_Entities_Conferences_TalkConferenceArtifacts
    sessionHallsArtifacts: Optional[Dict[str, Any]] = None  # Артефакты сессионных залов
    eventDescription: Optional[str] = None  # Описание цели встречи

class SkbKontur_Talk_Web_Entities_Conferences_TalkConferenceArtifacts(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Conferences.TalkConferenceArtifacts."""
    participants: Optional[List[SkbKontur_Talk_Api_Entities_TalkUserRef]] = None  # Список участников
    content: Optional[List[SkbKontur_Talk_ConferencesHistory_Entities_ConferenceContent]] = None  # Артефакты конференции
    title: Optional[str] = None  # Название
    chatChannelHasMessages: Optional[Dict[str, Any]] = None  # Признак наличия сообщений в каналах

class SkbKontur_Talk_Web_Entities_Conferences_TalkConferenceInfo(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Conferences.TalkConferenceInfo."""
    key: Optional[str] = None  # Ключ конференции
    roomName: Optional[str] = None  # Название комнаты
    startTime: Optional[datetime] = None  # Дата начала конференции
    endTime: Optional[datetime] = None  # Дата окончания конференции
    title: Optional[str] = None  # Заголовок
    isPlannedMeeting: Optional[bool] = None  # Была ли конференция запланированной
    containsDeepFakeDetections: Optional[bool] = None  # Признак конференции, проверенной на наличие дипфейков

class SkbKontur_Talk_Web_Entities_Conferences_TalkConferenceInfos(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Conferences.TalkConferenceInfos."""
    conferences: Optional[List[SkbKontur_Talk_Web_Entities_Conferences_TalkConferenceInfo]] = None

class SkbKontur_Talk_Web_Entities_Conferences_TalkEnrichedConference(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Conferences.TalkEnrichedConference."""
    key: Optional[str] = None  # Ключ конференции
    roomName: Optional[str] = None  # Название комнаты
    startTime: Optional[datetime] = None  # Дата начала конференции
    endTime: Optional[datetime] = None  # Дата окончания конференции
    title: Optional[str] = None  # Заголовок
    isPlannedMeeting: Optional[bool] = None  # Была ли конференция запланированной
    description: Optional[str] = None  # Описание
    artifacts: SkbKontur_Talk_Web_Entities_Conferences_TalkEnrichedConferenceArtifacts
    sessionHallsArtifacts: Optional[Dict[str, Any]] = None  # Артефакты сессионных залов
    containsDeepFakeDetections: Optional[bool] = None  # Признак конференции, проверенной на наличие дипфейков
    eventDescription: Optional[str] = None  # Описание цели встречи

class SkbKontur_Talk_Web_Entities_Conferences_TalkEnrichedConferenceArtifacts(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Conferences.TalkEnrichedConferenceArtifacts."""
    title: Optional[str] = None  # Название
    participants: Optional[List[SkbKontur_Talk_Api_Entities_TalkUserRef]] = None  # Список участников
    recordings: Optional[List[SkbKontur_Talk_Web_Entities_Recordings_TalkConferenceRecording]] = None  # Записи встречи
    polls: Optional[List[SkbKontur_Talk_Api_Entities_Poll_TalkPoll]] = None  # Опросы
    notes: Optional[List[SkbKontur_Talk_Notes_Api_Models_TalkNoteInfo]] = None  # Заметки
    messagesByChannel: Optional[Dict[str, Any]] = None  # Сообщения в каналах

class SkbKontur_Talk_Web_Entities_Domains_TalkDomainApplication(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Domains.TalkDomainApplication."""
    name: str  # Название приложения
    description: Optional[str] = None  # Описание приложения
    id: str  # Идентификатор api-ключа
    expiredAt: Optional[datetime] = None  # Дата действия ключа
    token: str  # Api Key
    scopes: List[SkbKontur_Talk_Web_Entities_Domains_TalkScope]  # Доступные области
    created: Optional[datetime] = None  # Дата создания
    createdBy: SkbKontur_Talk_Web_Entities_TalkUser
    modified: Optional[datetime] = None  # Дата обновления
    modifiedBy: SkbKontur_Talk_Web_Entities_TalkUser
    refreshedTokenBy: SkbKontur_Talk_Web_Entities_TalkUser
    lastActivityDate: Optional[datetime] = None  # Последняя активность ключа
    targetApiType: SkbKontur_Talk_Web_Entities_Domains_TalkTargetApiType
    internalApiName: SkbKontur_Talk_Web_Entities_Domains_TalkInternalApiName
    isReadOnly: Optional[bool] = None  # Признак, что ключ нельзя менять

class SkbKontur_Talk_Web_Entities_Domains_TalkDomainApplicationAccessInfo(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Domains.TalkDomainApplicationAccessInfo."""
    expiredAt: Optional[datetime] = None  # Срок действия ключа
    scopes: Optional[List[SkbKontur_Talk_Web_Entities_Domains_TalkScope]] = None  # Доступные области

class SkbKontur_Talk_Web_Entities_Domains_TalkDomainApplicationsList(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Domains.TalkDomainApplicationsList."""
    applications: Optional[List[SkbKontur_Talk_Web_Entities_Domains_TalkDomainApplication]] = None  # Коллекция API-ключей в пространстве

class SkbKontur_Talk_Web_Entities_Domains_TalkDomainStatistics(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Domains.TalkDomainStatistics."""
    created: Optional[datetime] = None  # С какого периода просмотреть статистику
    startDate: Optional[datetime] = None  # Начало периода статистики
    endDate: Optional[datetime] = None  # Окончание периода статистики
    statistics: Optional[Dict[str, Any]] = None  # Значения статистики

class SkbKontur_Talk_Web_Entities_Domains_TalkInternalApiName(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Domains.TalkInternalApiName."""
    pass

class SkbKontur_Talk_Web_Entities_Domains_TalkScope(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Domains.TalkScope."""
    type: SkbKontur_Talk_Web_Entities_Domains_TalkScopeType
    restrictionType: SkbKontur_Talk_Web_Entities_Domains_TalkScopeRestrictionType

class SkbKontur_Talk_Web_Entities_Domains_TalkScopeRestrictionType(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Domains.TalkScopeRestrictionType."""
    pass

class SkbKontur_Talk_Web_Entities_Domains_TalkScopeType(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Domains.TalkScopeType."""
    pass

class SkbKontur_Talk_Web_Entities_Domains_TalkTargetApiType(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Domains.TalkTargetApiType."""
    pass

class SkbKontur_Talk_Web_Entities_Features_TalkCalendarFeatureSettingsModify(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Features.TalkCalendarFeatureSettingsModify."""
    userName: Optional[str] = None  # Имя пользователя, параметр календаря EWS
    password: Optional[str] = None  # Пароль
    tenantId: Optional[str] = None  # Идентификатор владельца из Microsoft Azure
    clientId: Optional[str] = None  # Идентификатор приложения из Microsoft Azure
    clientSecret: Optional[str] = None  # Значение секрета для приложения из Microsoft Azure
    url: Optional[str] = None  # Адрес
    type: SkbKontur_Talk_Web_Entities_Calendar_TalkCalendarType
    ewsVersion: SkbKontur_Talk_Platform_UserDomains_Configuration_Calendar_EwsVersion
    calDavServerType: SkbKontur_Talk_Platform_UserDomains_Configuration_Calendar_CalDavServerType
    enableSyncPhoto: Optional[bool] = None  # Признак синхронизации фото пользователей в календаре и в Толке

class SkbKontur_Talk_Web_Entities_Kiosk_News_TalkKioskNews(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.News.TalkKioskNews."""
    newsList: Optional[List[SkbKontur_Talk_Web_Entities_Kiosk_News_TalkKioskNewsItem]] = None  # Коллекция новостей
    nextState: Optional[int] = None  # Флаг последней новости для следующих запросов с этого момента

class SkbKontur_Talk_Web_Entities_Kiosk_News_TalkKioskNewsItem(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.News.TalkKioskNewsItem."""
    id: Optional[str] = None  # Идентификатор запроса
    date: Optional[datetime] = None  # Время создания запроса
    type: SkbKontur_Talk_Kiosk_Domain_KioskNewsType
    comment: Optional[str] = None  # Комментарий запроса. Для вызова техподдержки всегда null
    kiosk: SkbKontur_Talk_Web_Entities_Kiosk_News_TalkKioskNewsKioskInfo

class SkbKontur_Talk_Web_Entities_Kiosk_News_TalkKioskNewsKioskInfo(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.News.TalkKioskNewsKioskInfo."""
    id: Optional[str] = None  # Идентификатор киоска, откуда поступил запрос
    title: Optional[str] = None  # Название киоска
    description: Optional[str] = None  # Путь до киоска. Вычисляется по дереву групп. Если группы не включены на пространстве - выводится описание киоска

class SkbKontur_Talk_Web_Entities_Kiosk_Screensaver_KioskRichScreensaverDto(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.Screensaver.KioskRichScreensaverDto."""
    key: Optional[str] = None  # Ключ заставки
    path: Optional[str] = None  # Относительный путь до заставки
    uploadDate: Optional[datetime] = None  # Дата загрузки

class SkbKontur_Talk_Web_Entities_Kiosk_Screensaver_KioskScreensaverDto(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.Screensaver.KioskScreensaverDto."""
    key: Optional[str] = None  # Ключ заставки
    path: Optional[str] = None  # Относительный путь до заставки

class SkbKontur_Talk_Web_Entities_Kiosk_Screensaver_TalkKioskRichScreensaverResponse(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.Screensaver.TalkKioskRichScreensaverResponse."""
    items: Optional[List[SkbKontur_Talk_Web_Entities_Kiosk_Screensaver_KioskRichScreensaverDto]] = None

class SkbKontur_Talk_Web_Entities_Kiosk_Screensaver_TalkKioskScreensaversResponse(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.Screensaver.TalkKioskScreensaversResponse."""
    items: Optional[List[SkbKontur_Talk_Web_Entities_Kiosk_Screensaver_KioskScreensaverDto]] = None

class SkbKontur_Talk_Web_Entities_Kiosk_Screensaver_TalkKioskUploadScreensaver(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.Screensaver.TalkKioskUploadScreensaver."""
    fileName: Optional[str] = None  # Имя файла
    screensaver: SkbKontur_Talk_Web_Entities_Kiosk_Screensaver_KioskRichScreensaverDto
    error: Optional[str] = None  # Ошибка

class SkbKontur_Talk_Web_Entities_Kiosk_Screensaver_TalkKioskUploadScreensaverResponse(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.Screensaver.TalkKioskUploadScreensaverResponse."""
    items: Optional[List[SkbKontur_Talk_Web_Entities_Kiosk_Screensaver_TalkKioskUploadScreensaver]] = None

class SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskAudioSettings(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskAudioSettings."""
    agc: Optional[bool] = None  # Включать автоматическую регулировку громкости микрофона.
    ns: Optional[bool] = None  # Включать шумоподавление.
    startMuted: Optional[bool] = None  # Подключаться с выключенным микрофоном.
    defaultSpeakerVolume: Optional[float] = None  # Громкость динамика по умолчанию
    preferredMic: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDevice
    preferredSpeaker: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDevice

class SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskCheckInSettings(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskCheckInSettings."""
    isEnabled: Optional[bool] = None  # Вкл\выкл
    isSoundAlertEnabled: Optional[bool] = None  # Вкл\выкл звукового оповещения
    waitAfterEventStart: Optional[float] = None  # Время после начала встречи для подтверждения занятости, в мс
    waitBeforeEventStart: Optional[float] = None  # Время до начала встречи для подтверждения занятости, в мс
    recurrenceEventRemoveEnabled: Optional[bool] = None  # Вкл\выкл удаление повторяющихся встреч
    recurrenceEventsSkipLimit: Optional[int] = None  # Кол-во допустимых пропусков повторяющейся встречи до удаления ряда
    isCheckOutEnabled: Optional[bool] = None  # Вкл\выкл завершение бронирования

class SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskConfiguration(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskConfiguration."""
    title: Optional[str] = None  # Название киоска
    description: Optional[str] = None  # Описание киоска
    calendarMailbox: Optional[str] = None  # Электронный адрес для интеграции с календарем киоска
    autoLaunch: Optional[bool] = None  # Разрешить автоматически запускать киоск при старте системы
    canClose: Optional[bool] = None  # Разрешать закрывать киоск
    autoUpdate: Optional[bool] = None  # Разрешать автообновление киоска
    idleTimeoutMinutes: Optional[int] = None  # Если пользователь закрыл киоск, то по истечении какого времени неактивности
(не шевелится мышь и нет нажатий клавиш) открывать киоск
    prolongIdleMinutes: Optional[int] = None  # Сколько минут не беспокоить пользователя, если он продлил время работы с ПК
    confirmActivitySeconds: Optional[int] = None  # Сколько секунд ждать до подтверждения активности пользователем, прежде чем открыть киоск повторно
    theme: SkbKontur_Talk_Web_Entities_Kiosk_TalkTheme
    windowMode: Optional[bool] = None  # Запускать в режиме окна
    wallpaperKeys: Optional[List[str]] = None  # Фоны
    screensaverKeys: Optional[List[str]] = None  # Заставки
    waitScreensaverShow: Optional[int] = None  # Время до показа заставки, в мс
    audio: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskAudioSettings
    video: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskVideoSettings
    updatesChannel: Optional[str] = None  # Канал обновлений приложения
    autoPip: Optional[bool] = None  # Авто картинка в картинке
    noToolbars: Optional[bool] = None  # Закрепление панелей тулбара
    joinLeaveNotifications: Optional[bool] = None  # Уведомление о подключении к встрече
    support: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskSupportSettings
    hideParticipantsWithoutVideo: Optional[bool] = None  # Скрыть участников без видео
    hideParticipantLabels: Optional[bool] = None  # Скрыть имена участников
    drinks: Optional[List[SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDrink]] = None  # Список напитков, доступных для заказа
    isFastReservationEnabled: Optional[bool] = None  # Вкл\выкл быстрое бронирование
    checkIn: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskCheckInSettings
    hideForBooking: Optional[bool] = None  # Скрыть для бронирования
    screens: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskScreensSettings

class SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDaemon(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskDaemon."""
    id: Optional[str] = None  # Идентификатор киоска
    kioskKey: Optional[str] = None  # Ключ киоска
    machineName: Optional[str] = None  # Имя машины, на которой запущен демон
    configuration: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskConfiguration
    isLaunched: Optional[bool] = None  # Активен ли киоск.
True, если дата последней синхронизации не позднее, чем за 15 минут от текущего времени
    createdDate: Optional[datetime] = None  # Дата последней активности
    lastActivityDate: Optional[datetime] = None  # Последняя дата активности демона
    version: Optional[str] = None  # Версия приложения Толк, используемая на киоске
    cameraDevices: Optional[List[SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDevice]] = None  # Доступные камеры
    microphoneDevices: Optional[List[SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDevice]] = None  # Доступные микрофоны
    speakerDevices: Optional[List[SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDevice]] = None  # Доступные динамики
    screenDevices: Optional[List[SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskScreenDevice]] = None  # Доступные экраны
    conferenceStatus: SkbKontur_Talk_Kiosk_Domain_KioskConferenceStatus
    kioskEquipmentCheckStatus: SkbKontur_Talk_Kiosk_Domain_KioskEquipmentCheckStatus
    status: SkbKontur_Talk_Kiosk_Domain_KioskDaemonStatus
    ignoreMassUpdate: Optional[bool] = None  # Признак игнорирования массовых обновлений
    groupKey: Optional[str] = None  # Ключ группы
    heartbeatRate: Optional[str] = None
    newLaunchUrl: Optional[str] = None  # Заменённый URL для запуска приложения на киоске

class SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDaemonCreateParameters(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskDaemonCreateParameters."""
    configuration: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskConfiguration
    groupKey: Optional[str] = None  # Местоположение в дереве групп
    isBlocked: Optional[bool] = None  # Заблокирован ли киоск.
True, если заблокирован и не может работать
    ignoreMassUpdate: Optional[bool] = None  # Игнорировать массовое обновление настроек киосков

class SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDaemonMassUpdateParameters(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskDaemonMassUpdateParameters."""
    audio: SkbKontur_Talk_Kiosk_Domain_KioskMassUpdateAudioSettings
    video: SkbKontur_Talk_Kiosk_Domain_KioskMassUpdateVideoSettings
    updatesChannel: Optional[str] = None  # Канал обновления
    autoUpdate: Optional[bool] = None  # Автоматическое обнаружение и установка новых версий приложения
    autoLaunch: Optional[bool] = None  # Автоматически запускать киоск при старте системы
    canClose: Optional[bool] = None  # Разрешить закрытие киоска
    autoPip: Optional[bool] = None  # Авто картинка в картинке
    noToolbars: Optional[bool] = None  # Закрепление панелей тулбара
    joinLeaveNotifications: Optional[bool] = None  # Уведомление о подключении к встрече
    ignoreMassUpdate: Optional[bool] = None  # Игнорировать массовые обновления
    wallpaperKeys: Optional[List[str]] = None  # Фоны
    screensaverKeys: Optional[List[str]] = None  # Заставки
    waitScreensaverShow: Optional[int] = None  # Время до показа заставки, в мс
    support: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskSupportSettings
    hideParticipantsWithoutVideo: Optional[bool] = None  # Скрыть участников без видео
    hideParticipantLabels: Optional[bool] = None  # Скрыть имена участников
    drinks: Optional[List[SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDrink]] = None  # Список напитков доступных для заказа
    isFastReservationEnabled: Optional[bool] = None  # Вкл\выкл быстрое бронирование
    checkIn: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskCheckInSettings
    hideForBooking: Optional[bool] = None  # Скрыть для бронирования
    screens: SkbKontur_Talk_Kiosk_Domain_KioskMassUpdateScreensSettings

class SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDaemonUpdateParameters(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskDaemonUpdateParameters."""
    configuration: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskConfiguration
    ignoreMassUpdate: Optional[bool] = None  # Игнорировать ли массовое обновление настроек киосков

class SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDevice(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskDevice."""
    label: Optional[str] = None  # Название
    deviceId: Optional[str] = None  # Идентификатор устройства

class SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDrink(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskDrink."""
    title: str  # Уникальное название напитка
    description: Optional[str] = None  # Описание

class SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskList(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskList."""
    kiosks: Optional[List[SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDaemon]] = None

class SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskMassUpdateRequest(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskMassUpdateRequest."""
    kioskIds: List[str]  # Идентификаторы киосков, к которым нужно применить массовое действие
    parameters: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDaemonMassUpdateParameters

class SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskScreenDevice(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskScreenDevice."""
    label: Optional[str] = None  # Название
    deviceId: Optional[str] = None  # Идентификатор устройства
    primary: Optional[bool] = None
    touchSupport: SkbKontur_Talk_Common_Data_DeviceTouchSupport

class SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskScreensSettings(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskScreensSettings."""
    useSecondScreenForScreenShare: Optional[bool] = None  # Использовать 2 экран для презентаций
    embeddedControllerEnabled: Optional[bool] = None  # Включено ли использование встроенного контроллера (Yealink)
    embeddedControllerScreen: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDevice

class SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskSupportSettings(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskSupportSettings."""
    supportRequestEnabled: Optional[bool] = None  # Вызов поддержки включен
    description: Optional[str] = None  # Сопроводительный текст вызова поддержки

class SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskVideoSettings(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkKioskVideoSettings."""
    wideCamera: Optional[bool] = None  # Использовать широкоформатное видео с камеры.
    startMuted: Optional[bool] = None  # Подключаться с выключенной камерой.
    recvVideoQuality: Optional[int] = None  # Запрашиваемое качество видео
    sendVideoQuality: Optional[int] = None  # Отправляемое качество видео
    bindToPPI: Optional[bool] = None
    preferredCamera: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDevice
    preferredVideoCapture: SkbKontur_Talk_Web_Entities_Kiosk_TalkKioskDevice

class SkbKontur_Talk_Web_Entities_Kiosk_TalkTheme(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.TalkTheme."""
    pass

class SkbKontur_Talk_Web_Entities_Kiosk_Wallpaper_TalkKioskRichWallpaper(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.Wallpaper.TalkKioskRichWallpaper."""
    key: Optional[str] = None  # Ключ фона
    path: Optional[str] = None  # Относительный путь до фона
    isEnabledByDefault: Optional[bool] = None  # Признак включенности по умолчанию
    source: SkbKontur_Talk_Kiosk_Models_Wallpaper_KioskWallpaperSource
    uploadDate: Optional[datetime] = None  # Дата загрузки
    modified: Optional[datetime] = None  # Дата обновления

class SkbKontur_Talk_Web_Entities_Kiosk_Wallpaper_TalkKioskRichWallpaperResponse(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.Wallpaper.TalkKioskRichWallpaperResponse."""
    items: Optional[List[SkbKontur_Talk_Web_Entities_Kiosk_Wallpaper_TalkKioskRichWallpaper]] = None

class SkbKontur_Talk_Web_Entities_Kiosk_Wallpaper_TalkKioskUploadWallpaper(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.Wallpaper.TalkKioskUploadWallpaper."""
    fileName: Optional[str] = None  # Имя файла
    wallpaper: SkbKontur_Talk_Web_Entities_Kiosk_Wallpaper_TalkKioskRichWallpaper
    error: Optional[str] = None  # Ошибка

class SkbKontur_Talk_Web_Entities_Kiosk_Wallpaper_TalkKioskUploadWallpaperResponse(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.Wallpaper.TalkKioskUploadWallpaperResponse."""
    items: Optional[List[SkbKontur_Talk_Web_Entities_Kiosk_Wallpaper_TalkKioskUploadWallpaper]] = None

class SkbKontur_Talk_Web_Entities_Kiosk_Wallpaper_TalkKioskWallpaper(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.Wallpaper.TalkKioskWallpaper."""
    key: Optional[str] = None  # Ключ фона
    path: Optional[str] = None  # Относительный путь до фона

class SkbKontur_Talk_Web_Entities_Kiosk_Wallpaper_TalkKioskWallpaperSettingsRequest(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.Wallpaper.TalkKioskWallpaperSettingsRequest."""
    wallpapers: Optional[List[str]] = None  # Коллекция идентификаторов фонов

class SkbKontur_Talk_Web_Entities_Kiosk_Wallpaper_TalkKioskWallpapersResponse(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Kiosk.Wallpaper.TalkKioskWallpapersResponse."""
    items: Optional[List[SkbKontur_Talk_Web_Entities_Kiosk_Wallpaper_TalkKioskWallpaper]] = None

class SkbKontur_Talk_Web_Entities_Recordings_Access_PatchRecordAccessRequest(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Recordings.Access.PatchRecordAccessRequest."""
    userAccesses: List[SkbKontur_Talk_Web_Entities_Access_PatchUsersAccessRequest]  # Точечные доступы
    linkAccess: SkbKontur_Talk_Web_Entities_Recordings_Access_TalkRecordLinkAccess

class SkbKontur_Talk_Web_Entities_Recordings_Access_RecordsResourceAccessResponse(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Recordings.Access.RecordsResourceAccessResponse."""
    userAccesses: List[SkbKontur_Talk_Web_Entities_Access_UsersAccessResponse]  # Точечные доступы
    linkAccess: SkbKontur_Talk_Web_Entities_Recordings_Access_TalkRecordLinkAccess

class SkbKontur_Talk_Web_Entities_Recordings_Access_TalkRecordLinkAccess(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Recordings.Access.TalkRecordLinkAccess."""
    scope: SkbKontur_Talk_Resources_Access_LinkAccess_ResourceLinkAccessScope

class SkbKontur_Talk_Web_Entities_Recordings_TalkConferenceRecording(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Recordings.TalkConferenceRecording."""
    id: Optional[str] = None  # Идентификатор
    title: Optional[str] = None  # Название
    description: Optional[str] = None  # Описание
    previewImage: SkbKontur_Talk_Web_Entities_Recordings_TalkRecordingPreview
    createdDate: Optional[datetime] = None  # Дата записи
    createdBy: SkbKontur_Talk_Web_Entities_TalkUser
    duration: Optional[int] = None  # Продолжительность
    progress: Optional[int] = None  # Процент обработки
    status: SkbKontur_Talk_Recordings_Domain_VideoMediaUploadStatus
    frameSize: SkbKontur_Talk_Web_Entities_Recordings_TalkMediaSize
    allowAnonymousAccess: Optional[bool] = None  # Признак доступности анонимам
    participants: Optional[List[SkbKontur_Talk_Api_Entities_TalkUserRef]] = None  # Участники конференции
    participantsCount: Optional[int] = None  # Количество участников
    commentsCount: Optional[int] = None  # Число комментариев
    hasAudioRecord: Optional[bool] = None  # У записи есть аудио
    qualities: Optional[List[SkbKontur_Talk_Web_Entities_Recordings_TalkVideoQuality]] = None  # Файлы разного качества
    transcription: SkbKontur_Talk_SpeechCore_Api_Models_Transcription_TalkTranscription
    conferenceKey: Optional[str] = None  # Ключ конференции
    notesCount: Optional[int] = None  # Число заметок
    isStream: Optional[bool] = None  # Запись Стрима

class SkbKontur_Talk_Web_Entities_Recordings_TalkConferenceRecordingUpdateParams(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Recordings.TalkConferenceRecordingUpdateParams."""
    title: str  # Название записи. Максимально допустимая длина — 512
    description: Optional[str] = None  # Описание. Максимально допустимая длина — 4096
    allowAnonymousAccess: Optional[bool] = None  # Доступ к записи у анонимов. По умолчанию — false

class SkbKontur_Talk_Web_Entities_Recordings_TalkDomainConferenceRecording(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Recordings.TalkDomainConferenceRecording."""
    id: Optional[str] = None  # Идентификатор записи
    key: Optional[str] = None  # Ключ записи
    title: Optional[str] = None  # Название записи
    createdDate: Optional[datetime] = None  # Дата создания записи (загрузки на сервер после окончания)
    createdBy: SkbKontur_Talk_Web_Entities_TalkUser
    roomName: Optional[str] = None  # Название комнаты
    participantsCount: Optional[int] = None  # Количество участников в записи
    size: Optional[int] = None  # Отображаемый размер записи в хранилище
    duration: Optional[int] = None  # Продолжительность
    canBeRemoved: Optional[bool] = None  # Может ли элемент быть удален
    participants: Optional[List[SkbKontur_Talk_Api_Entities_TalkUserBaseInfoRef]] = None  # Участники
    allowAnonymousAccess: Optional[bool] = None  # Разрешен ли доступ внешних участников

class SkbKontur_Talk_Web_Entities_Recordings_TalkDomainRecordingsList(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Recordings.TalkDomainRecordingsList."""
    recordings: Optional[List[SkbKontur_Talk_Web_Entities_Recordings_TalkDomainConferenceRecording]] = None

class SkbKontur_Talk_Web_Entities_Recordings_TalkMediaSize(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Recordings.TalkMediaSize."""
    width: Optional[int] = None  # Ширина
    height: Optional[int] = None  # Высота

class SkbKontur_Talk_Web_Entities_Recordings_TalkRecordingPreview(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Recordings.TalkRecordingPreview."""
    fileUrl: Optional[str] = None  # Путь до файла
    size: SkbKontur_Talk_Web_Entities_Recordings_TalkMediaSize

class SkbKontur_Talk_Web_Entities_Recordings_TalkVideoQuality(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Recordings.TalkVideoQuality."""
    status: SkbKontur_Talk_Recordings_Domain_VideoMediaUploadStatus
    progress: Optional[int] = None  # Процент загрузки
    fileUrl: Optional[str] = None  # Путь до файла
    size: SkbKontur_Talk_Web_Entities_Recordings_TalkMediaSize
    name: Optional[str] = None

class SkbKontur_Talk_Web_Entities_Rooms_LockRoomRequest(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.LockRoomRequest."""
    pinCode: Optional[str] = None  # ПИН-код. Допустимая длина: от 4 до 6 символов. Только цифры

class SkbKontur_Talk_Web_Entities_Rooms_Masking_TalkMaskingSettings(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.Masking.TalkMaskingSettings."""
    nameMaskingMode: SkbKontur_Talk_Web_Entities_Rooms_Masking_TalkNameMaskingMode
    postMaskingMode: SkbKontur_Talk_Web_Entities_Rooms_Masking_TalkPostMaskingMode
    showAdditionalInfo: bool  # Нужно ли показывать дополнительную информацию пользователей

class SkbKontur_Talk_Web_Entities_Rooms_Masking_TalkNameMaskingMode(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.Masking.TalkNameMaskingMode."""
    pass

class SkbKontur_Talk_Web_Entities_Rooms_Masking_TalkPostMaskingMode(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.Masking.TalkPostMaskingMode."""
    pass

class SkbKontur_Talk_Web_Entities_Rooms_RoomSipSettings(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.RoomSipSettings."""
    sipNumber: Optional[str] = None  # Номер комнаты
    sipUri: Optional[str] = None  # Полный путь sip шлюза
    phoneNumbers: Optional[List[str]] = None  # Номера телефонов

class SkbKontur_Talk_Web_Entities_Rooms_TalkChatChannelRoomsSettings(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.TalkChatChannelRoomsSettings."""
    enabled: Optional[bool] = None  # Включен
    allowedUsers: Optional[List[SkbKontur_Talk_Api_Entities_TalkUserRef]] = None  # Пользователи, имеющие доступ

class SkbKontur_Talk_Web_Entities_Rooms_TalkChatChannelSettings(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.TalkChatChannelSettings."""
    enabled: Optional[bool] = None  # Включен
    allowedUsers: Optional[List[SkbKontur_Talk_Web_Entities_Rooms_TalkChatChannelUserRef]] = None  # Пользователи, имеющие доступ

class SkbKontur_Talk_Web_Entities_Rooms_TalkChatChannelUserRef(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.TalkChatChannelUserRef."""
    userKey: Optional[str] = None
    anonymousId: Optional[str] = None

class SkbKontur_Talk_Web_Entities_Rooms_TalkInputPolicy(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.TalkInputPolicy."""
    pass

class SkbKontur_Talk_Web_Entities_Rooms_TalkLanguagePair(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.TalkLanguagePair."""
    from_: Optional[str] = None  # С какого языка
    to: Optional[str] = None  # На какой язык
    translators: Optional[List[SkbKontur_Talk_Api_Entities_TalkUserRef]] = None  # Переводчики

class SkbKontur_Talk_Web_Entities_Rooms_TalkLanguagePairUpdateModel(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.TalkLanguagePairUpdateModel."""
    from_: str
    to: str
    translators: List[SkbKontur_Talk_Web_Entities_Rooms_TalkTranslator]

class SkbKontur_Talk_Web_Entities_Rooms_TalkRoom(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.TalkRoom."""
    roomName: str  # Ключ комнаты
    title: Optional[str] = None  # Заголовок
    description: Optional[str] = None  # Описание
    sessionHalls: Optional[List[SkbKontur_Talk_Web_Entities_Rooms_TalkSessionHallInfo]] = None  # Сессионные залы
    enableSessionHall: Optional[bool] = None  # Признак доступности сессионных залов
    disableHallsMoves: Optional[bool] = None  # Запретить перемещение не модераторов между группами
    enableLobby: Optional[bool] = None  # Включить комнату ожидания
    stageConferenceId: str  # ConferenceId сцены
    moderators: Optional[List[SkbKontur_Talk_Web_Entities_TalkUser]] = None  # Неанонимные модераторы
    anonymousModerators: Optional[List[SkbKontur_Talk_Web_Entities_TalkAnonymous]] = None  # Анонимные модераторы
    allowAnonymous: Optional[bool] = None  # Разрешить подключение анонимных пользователей
    anonymousAccessExpirationDate: Optional[datetime] = None  # Срок для возможности подключения внешних участников
    anonymousAccessModifiedDate: Optional[datetime] = None  # Последнее изменение срока для возможности подключения внешних участников
    audioPolicy: SkbKontur_Talk_Web_Entities_Rooms_TalkInputPolicy
    videoPolicy: SkbKontur_Talk_Web_Entities_Rooms_TalkInputPolicy
    screenSharePolicy: SkbKontur_Talk_Web_Entities_Rooms_TalkInputPolicy
    securityType: SkbKontur_Talk_Web_Entities_Rooms_TalkRoomSecurityType
    pinCode: Optional[str] = None  # Пин код
    isModerator: Optional[bool] = None  # Является ли пользователем модератором
    conferenceId: str  # Идентификатор Конференции для подключения
    sipSettings: SkbKontur_Talk_Web_Entities_Rooms_RoomSipSettings
    usersOnline: Optional[int] = None  # Количество подключений
    onlineUsers: Optional[List[SkbKontur_Talk_Api_Entities_TalkUserRef]] = None  # Информация о пользователях
    roomStream: SkbKontur_Talk_Web_Entities_Rooms_TalkRoomStream
    simultaneousTranslation: SkbKontur_Talk_Web_Entities_Rooms_TalkSimultaneousTranslation
    chatChannelSettings: SkbKontur_Talk_Web_Entities_Rooms_TalkChatChannelRoomsSettings
    showSpeakerInfo: Optional[bool] = None
    soundpadEnabled: Optional[bool] = None  # Флаг для включения звуковой панели
    disableVirtualBackgrounds: Optional[bool] = None  # Запретить виртуальные фоны в комнате
    maskingSettings: SkbKontur_Talk_Web_Entities_Rooms_Masking_TalkMaskingSettings
    autoRunDeepFakeDetection: Optional[bool] = None  # Настройка автоматического запуска детекции дипфейков в комнате

class SkbKontur_Talk_Web_Entities_Rooms_TalkRoomParams(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.TalkRoomParams."""
    title: Optional[str] = None  # Заголовок
    description: Optional[str] = None  # Описание
    moderatorKeys: Optional[List[str]] = None  # Неанонимные модераторы
    anonymousModeratorIds: Optional[List[str]] = None  # Анонимные модераторы
    anonymousAccessExpirationDate: Optional[datetime] = None  # Разрешить подключение анонимных пользователей до даты
    allowAnonymous: Optional[bool] = None
    disableVirtualBackgrounds: Optional[bool] = None  # Запретить виртуальные фоны в комнате
    enableSessionHalls: Optional[bool] = None  # Флаг включения сессионых залов
    disableHallsMoves: Optional[bool] = None  # Запретить перемещение не модераторов между группами
    enableLobby: Optional[bool] = None  # Флаг включения вход по запросу
    audioPolicy: SkbKontur_Talk_Web_Entities_Rooms_TalkInputPolicy
    videoPolicy: SkbKontur_Talk_Web_Entities_Rooms_TalkInputPolicy
    screenSharePolicy: SkbKontur_Talk_Web_Entities_Rooms_TalkInputPolicy
    chatChannelSettings: SkbKontur_Talk_Web_Entities_Rooms_TalkChatChannelSettings
    showSpeakerInfo: Optional[bool] = None
    soundpadEnabled: Optional[bool] = None  # Флаг для включения звуковой панели
    maskingSettings: SkbKontur_Talk_Web_Entities_Rooms_Masking_TalkMaskingSettings
    autoRunDeepFakeDetection: Optional[bool] = None  # Настройка автоматического запуска детекции дипфейков в комнате

class SkbKontur_Talk_Web_Entities_Rooms_TalkRoomSecurityType(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.TalkRoomSecurityType."""
    pass

class SkbKontur_Talk_Web_Entities_Rooms_TalkRoomStream(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.TalkRoomStream."""
    title: Optional[str] = None  # Название трансляции
    expirationDate: Optional[datetime] = None  # Срок действия стрима
    allowAnonymous: Optional[bool] = None  # Доступен ли стрим внешним участникам
    isEnabled: Optional[bool] = None  # Включена ли трансляция
    isActive: Optional[bool] = None  # Флаг есть ли активные трансляции в данный момент
    streamKey: Optional[str] = None  # Ключ к зрительному залу
    viewersCount: Optional[int] = None  # Количество участников в зрительном зале
    playListSource: Optional[str] = None  # Ссылка на текущий плейлист
    playlistId: Optional[str] = None  # Идентификатор последнего плейлиста стрима

class SkbKontur_Talk_Web_Entities_Rooms_TalkSessionHallInfo(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.TalkSessionHallInfo."""
    conferenceId: Optional[str] = None  # Идентификатор конференции для подключения
    chatRoom: Optional[str] = None  # Идентификатор подключения к чату сессионной комнаты
    onlineUsersCount: Optional[int] = None  # Количество пользователей онлайн
    onlineUsers: Optional[List[SkbKontur_Talk_Api_Entities_TalkUserRef]] = None  # Подключенные пользователи
    id: Optional[str] = None  # Идентификатор сессионного зала
    users: Optional[List[SkbKontur_Talk_Api_Entities_TalkUserRef]] = None  # Пользователи сессионного зала
    title: Optional[str] = None  # Имя сессионного зала
    color: Optional[str] = None  # Цвет группы

class SkbKontur_Talk_Web_Entities_Rooms_TalkSimultaneousTranslation(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.TalkSimultaneousTranslation."""
    enabled: Optional[bool] = None  # Включение синхронного перевода
    languagePairs: Optional[List[SkbKontur_Talk_Web_Entities_Rooms_TalkLanguagePair]] = None  # Языковые пары для синхронного перевода

class SkbKontur_Talk_Web_Entities_Rooms_TalkSimultaneousTranslationUpdateRequest(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.TalkSimultaneousTranslationUpdateRequest."""
    enabled: bool
    languagePairs: List[SkbKontur_Talk_Web_Entities_Rooms_TalkLanguagePairUpdateModel]

class SkbKontur_Talk_Web_Entities_Rooms_TalkTranslator(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Rooms.TalkTranslator."""
    anonymousId: Optional[str] = None
    anonymousName: Optional[str] = None
    userKey: Optional[str] = None
    isAnonymous: Optional[bool] = None

class SkbKontur_Talk_Web_Entities_Statistics_RoomStatisticsReport(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Statistics.RoomStatisticsReport."""
    roomName: Optional[str] = None  # Ключ комнаты
    from_: Optional[datetime] = None  # Дата и время начала периода, за который запрошен отчет
    to: Optional[datetime] = None  # Дата и время окончания периода, за который запрошен отчет
    participantCount: Optional[int] = None  # Количество участников в комнате
    participantTotalDurations: Optional[List[SkbKontur_Talk_Rooms_Statistics_Reports_Models_ParticipantTotalDurationModel]] = None  # Статистика по пользователям
    roomParticipants: Optional[List[SkbKontur_Talk_Rooms_Statistics_Reports_Models_RoomStatisticsParticipantModel]] = None  # Статистика по времени входа и выхода
    streamViewers: Optional[List[SkbKontur_Talk_Rooms_Statistics_Reports_Models_Stream_StreamStatisticsViewerModel]] = None  # Статистика по зрителям, если комната использовалась для трансляций в зрительный зал
    metrics: SkbKontur_Talk_Rooms_Statistics_Reports_Models_RoomStatisticsReportMetricsModel

class SkbKontur_Talk_Web_Entities_Surveys_TalkCreateOrUpdateSurveyRequest(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Surveys.TalkCreateOrUpdateSurveyRequest."""
    name: str  # Название опроса
    url: str  # Адрес опроса
    frequency: SkbKontur_Talk_Web_Entities_Surveys_TalkSurveyFrequency
    period: SkbKontur_Talk_Web_Entities_Surveys_TalkSurveyPeriod

class SkbKontur_Talk_Web_Entities_Surveys_TalkSurvey(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Surveys.TalkSurvey."""
    id: str  # Идентификатор опроса
    name: str  # Название опроса
    url: str  # Адрес опроса
    frequency: SkbKontur_Talk_Web_Entities_Surveys_TalkSurveyFrequency
    period: SkbKontur_Talk_Web_Entities_Surveys_TalkSurveyPeriod
    isPublished: Optional[bool] = None  # Опубликован ли опрос

class SkbKontur_Talk_Web_Entities_Surveys_TalkSurveyFrequency(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Surveys.TalkSurveyFrequency."""
    pass

class SkbKontur_Talk_Web_Entities_Surveys_TalkSurveyList(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Surveys.TalkSurveyList."""
    entities: Optional[List[SkbKontur_Talk_Web_Entities_Surveys_TalkSurvey]] = None  # Список опросов

class SkbKontur_Talk_Web_Entities_Surveys_TalkSurveyPeriod(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.Surveys.TalkSurveyPeriod."""
    startDate: datetime  # Дата старта опроса
    endDate: datetime  # Дата окончания опроса

class SkbKontur_Talk_Web_Entities_TalkAnonymous(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkAnonymous."""
    anonymousId: Optional[str] = None  # Идентификатор анонима
    anonymousName: Optional[str] = None  # Имя анонима

class SkbKontur_Talk_Web_Entities_TalkAuditLogResponse(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkAuditLogResponse."""
    totalCount: Optional[int] = None  # Общее количество событий за указанный промежуток времени
    events: Optional[List[SkbKontur_Talk_AuditLog_Entities_AuditLogEvent]] = None  # События

class SkbKontur_Talk_Web_Entities_TalkAvatarInfo(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkAvatarInfo."""
    width: Optional[int] = None  # Ширина изображения
    height: Optional[int] = None  # Высота изображения
    face: SkbKontur_Talk_Web_Entities_TalkFaceRectangle
    contentHash: Optional[str] = None  # Хеш аватара

class SkbKontur_Talk_Web_Entities_TalkConferencesOnlineStatistics(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkConferencesOnlineStatistics."""
    usersCount: Optional[int] = None  # Количество активных пользователей
    conferencesCount: Optional[int] = None  # Количество активных конференций

class SkbKontur_Talk_Web_Entities_TalkFaceRectangle(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkFaceRectangle."""
    x: Optional[int] = None  # X-координата левого верхнего угла прямоугольника
    y: Optional[int] = None  # Y-координата левого верхнего угла прямоугольника
    width: Optional[int] = None  # Ширина
    height: Optional[int] = None  # Высота

class SkbKontur_Talk_Web_Entities_TalkKiosksOnlineStatistics(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkKiosksOnlineStatistics."""
    totalKioskConferencesCount: Optional[int] = None  # Количество киосков, подключенных к конференциям

class SkbKontur_Talk_Web_Entities_TalkOnlineCounters(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkOnlineCounters."""
    usersCount: Optional[int] = None  # Общее количество участников конференций
    conferencesCount: Optional[int] = None  # Общее количество конференций
    totalKioskConferencesCount: Optional[int] = None  # Общее количество киосков, находящихся в конференции в текущий момент

class SkbKontur_Talk_Web_Entities_TalkPage_SkbKontur_Talk_Web_Entities_Recordings_TalkDomainConferenceRecording(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkPage_SkbKontur.Talk.Web.Entities.Recordings.TalkDomainConferenceRecording."""
    entities: Optional[List[SkbKontur_Talk_Web_Entities_Recordings_TalkDomainConferenceRecording]] = None
    nextPageToken: Optional[str] = None
    prevPageToken: Optional[str] = None

class SkbKontur_Talk_Web_Entities_TalkRecordingsOnlineStatistics(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkRecordingsOnlineStatistics."""
    totalActiveRecordings: Optional[int] = None  # Количество идущих записей

class SkbKontur_Talk_Web_Entities_TalkRecordingsStatistics(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkRecordingsStatistics."""
    recordingsDurationMinutes: Optional[int] = None  # Длительность записей (в минутах)

class SkbKontur_Talk_Web_Entities_TalkRoleInfo(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkRoleInfo."""
    id: Optional[str] = None  # Идентификатор роли
    title: Optional[str] = None  # Название роли

class SkbKontur_Talk_Web_Entities_TalkStreamsOnlineStatistics(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkStreamsOnlineStatistics."""
    activeStreams: Optional[int] = None  # Количество идущих трансляций
    activeStreamsViewers: Optional[int] = None  # Количество зрителей трансляций в зрительных залах

class SkbKontur_Talk_Web_Entities_TalkTotalRecordingSizeStatistics(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkTotalRecordingSizeStatistics."""
    totalRecordingsSizeMb: Optional[int] = None  # Объем записей в облачном хранилище (в мегабайтах)

class SkbKontur_Talk_Web_Entities_TalkUser(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkUser."""
    userType: SkbKontur_Talk_Web_Entities_TalkUserType
    login: Optional[str] = None  # Логин
    hasEmail: Optional[bool] = None  # Признак наличия адреса электронной почты в профиле
    firstname: Optional[str] = None  # Имя
    surname: Optional[str] = None  # Фамилия
    patronymic: Optional[str] = None  # Отчество
    department: Optional[str] = None  # Отдел
    disabled: Optional[bool] = None  # Имеет ли пользователь доступ к домену
    deletedBySelf: Optional[bool] = None  # Признак удаления
    roles: Optional[List[str]] = None  # Роли пользователя
    roleInfos: Optional[List[SkbKontur_Talk_Web_Entities_TalkRoleInfo]] = None  # Роли пользователя с описаниями из ролевой модели
    key: Optional[str] = None  # Внешний ключ пользователя
    post: Optional[str] = None  # Должность
    avatarUrl: Optional[str] = None  # Ссылка на аватар
    profileUrl: Optional[str] = None  # Ссылка на внешний профиль
    hasMobilePhone: Optional[bool] = None  # Признак наличия мобильного телефона в профиле
    hasInnerPhone: Optional[bool] = None  # Признак наличия внутреннего номера в профиле
    avatarInfo: SkbKontur_Talk_Web_Entities_TalkAvatarInfo
    status: SkbKontur_Talk_Web_Entities_TalkUserStatus
    removed: Optional[bool] = None  # Пользователь удален
    hidden: Optional[bool] = None  # Пользователь скрыт
    email: Optional[str] = None  # Электронная почта
    features: Optional[List[str]] = None  # Доступные пользователю функциональности
    mobilePhone: Optional[str] = None  # Мобильный телефон
    innerPhone: Optional[str] = None  # Внутренний номер сотрудника

class SkbKontur_Talk_Web_Entities_TalkUserBaseInfo(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkUserBaseInfo."""
    userType: SkbKontur_Talk_Web_Entities_TalkUserType
    login: Optional[str] = None  # Логин
    hasEmail: Optional[bool] = None  # Признак наличия адреса электронной почты в профиле
    firstname: Optional[str] = None  # Имя
    surname: Optional[str] = None  # Фамилия
    patronymic: Optional[str] = None  # Отчество
    department: Optional[str] = None  # Отдел
    disabled: Optional[bool] = None  # Имеет ли пользователь доступ к домену
    deletedBySelf: Optional[bool] = None  # Признак удаления
    roles: Optional[List[str]] = None  # Роли пользователя
    roleInfos: Optional[List[SkbKontur_Talk_Web_Entities_TalkRoleInfo]] = None  # Роли пользователя с описаниями из ролевой модели
    key: Optional[str] = None  # Внешний ключ пользователя
    post: Optional[str] = None  # Должность
    avatarUrl: Optional[str] = None  # Ссылка на аватар
    profileUrl: Optional[str] = None  # Ссылка на внешний профиль
    hasMobilePhone: Optional[bool] = None  # Признак наличия мобильного телефона в профиле
    hasInnerPhone: Optional[bool] = None  # Признак наличия внутреннего номера в профиле
    avatarInfo: SkbKontur_Talk_Web_Entities_TalkAvatarInfo
    status: SkbKontur_Talk_Web_Entities_TalkUserStatus
    removed: Optional[bool] = None  # Пользователь удален
    hidden: Optional[bool] = None  # Пользователь скрыт

class SkbKontur_Talk_Web_Entities_TalkUserParams(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkUserParams."""
    firstname: str  # Имя
    surname: Optional[str] = None  # Фамилия
    patronymic: Optional[str] = None  # Отчество
    department: Optional[str] = None  # Отдел
    post: Optional[str] = None  # Должность
    mobilePhone: Optional[str] = None  # Мобильный номер
    innerPhone: Optional[str] = None  # Дополнительный номер
    townPhone: Optional[str] = None  # Городской номер
    login: Optional[str] = None  # Логин
    email: Optional[str] = None  # Электронная почта
    avatarUrl: Optional[str] = None  # Ссылка на изображение профиля
    profileUrl: Optional[str] = None  # Ссылка на профиль
    avatarInfo: SkbKontur_Talk_Web_Entities_TalkAvatarInfo
    userKey: Optional[str] = None  # Ключ пользователя

class SkbKontur_Talk_Web_Entities_TalkUserPermissions(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkUserPermissions."""
    disabled: Optional[bool] = None  # Имеет ли пользователь доступ к домену

class SkbKontur_Talk_Web_Entities_TalkUserScanResult(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkUserScanResult."""
    users: Optional[List[SkbKontur_Talk_Web_Entities_TalkUser]] = None  # Список пользователей
    offset: Optional[str] = None  # Смещение

class SkbKontur_Talk_Web_Entities_TalkUserSearchResult(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkUserSearchResult."""
    users: Optional[List[SkbKontur_Talk_Web_Entities_TalkUser]] = None  # Коллекция пользователей

class SkbKontur_Talk_Web_Entities_TalkUserStatus(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkUserStatus."""
    pass

class SkbKontur_Talk_Web_Entities_TalkUserType(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.TalkUserType."""
    pass

class SkbKontur_Talk_Web_Entities_UserRoles_TalkChangeDefaultRoleRequest(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.UserRoles.TalkChangeDefaultRoleRequest."""
    permissions: Optional[List[SkbKontur_Talk_Web_Entities_UserRoles_TalkPermissionRef]] = None  # Список разрешений

class SkbKontur_Talk_Web_Entities_UserRoles_TalkDefaultRoleType(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.UserRoles.TalkDefaultRoleType."""
    pass

class SkbKontur_Talk_Web_Entities_UserRoles_TalkPermission(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.UserRoles.TalkPermission."""
    productId: Optional[str] = None  # Идентификатор связанного сервиса
    permissionId: Optional[str] = None  # Идентификатор разрешения
    title: Optional[str] = None  # Название разрешения
    constructorVisible: Optional[bool] = None  # Признак отображения разрешения в конструкторе ролей

class SkbKontur_Talk_Web_Entities_UserRoles_TalkPermissionRef(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.UserRoles.TalkPermissionRef."""
    productId: Optional[str] = None  # Идентификатор связанного сервиса
    permissionId: Optional[str] = None  # Идентификатор разрешения

class SkbKontur_Talk_Web_Entities_UserRoles_TalkProductPermissions(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.UserRoles.TalkProductPermissions."""
    productId: Optional[str] = None  # Идентификатор продукта
    productTitle: Optional[str] = None  # Название продукта
    permissions: Optional[List[SkbKontur_Talk_Web_Entities_UserRoles_TalkPermission]] = None  # Список разрешений продуктов

class SkbKontur_Talk_Web_Entities_UserRoles_TalkUserChangeRolesRequest(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.UserRoles.TalkUserChangeRolesRequest."""
    addedRoleIds: Optional[List[str]] = None  # Идентификаторы добавляемых ролей
    removedRoleIds: Optional[List[str]] = None  # Идентификаторы удаляемых ролей

class SkbKontur_Talk_Web_Entities_UserRoles_TalkUserRole(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.UserRoles.TalkUserRole."""
    roleId: Optional[str] = None  # Идентификатор роли
    title: Optional[str] = None  # Название роли
    description: Optional[str] = None  # Описание
    editable: Optional[bool] = None  # Признак редактируемой роли
    permissions: Optional[List[SkbKontur_Talk_Web_Entities_UserRoles_TalkUserRolePermission]] = None  # Массив разрешений роли
    disabled: Optional[bool] = None  # Признак деактивации роли
    usersCount: Optional[int] = None  # Количество пользователей, которым назначена роль

class SkbKontur_Talk_Web_Entities_UserRoles_TalkUserRoleCreateRequest(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.UserRoles.TalkUserRoleCreateRequest."""
    title: str  # Название роли
    description: str  # Описание роли
    permissions: List[SkbKontur_Talk_Web_Entities_UserRoles_TalkUserRolePermissionValue]  # Список разрешений роли

class SkbKontur_Talk_Web_Entities_UserRoles_TalkUserRoleDescription(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.UserRoles.TalkUserRoleDescription."""
    roleId: Optional[str] = None  # Идентификатор роли
    title: Optional[str] = None  # Название роли
    description: Optional[str] = None  # Описание
    editable: Optional[bool] = None  # Признак редактируемой роли
    permissions: Optional[List[SkbKontur_Talk_Web_Entities_UserRoles_TalkUserRolePermission]] = None  # Массив разрешений роли

class SkbKontur_Talk_Web_Entities_UserRoles_TalkUserRoleInfo(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.UserRoles.TalkUserRoleInfo."""
    roleId: Optional[str] = None  # Идентификатор роли
    title: Optional[str] = None  # Название роли
    description: Optional[str] = None  # Описание
    editable: Optional[bool] = None  # Признак редактируемой роли

class SkbKontur_Talk_Web_Entities_UserRoles_TalkUserRolePermission(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.UserRoles.TalkUserRolePermission."""
    productId: Optional[str] = None  # Идентификатор связанного сервиса
    permissionId: Optional[str] = None  # Идентификатор разрешения
    title: Optional[str] = None  # Название разрешения
    constructorVisible: Optional[bool] = None  # Признак отображения разрешения в конструкторе ролей
    disabled: Optional[bool] = None  # Признак деактивированного разрешения

class SkbKontur_Talk_Web_Entities_UserRoles_TalkUserRolePermissionValue(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.UserRoles.TalkUserRolePermissionValue."""
    productId: str  # Идентификатор продукта
    permissionId: str  # Идентификатор разрешения
    disabled: Optional[bool] = None  # Признак деактивированного разрешения

class SkbKontur_Talk_Web_Entities_UserRoles_TalkUserRoleRef(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.UserRoles.TalkUserRoleRef."""
    roleId: Optional[str] = None  # Идентификатор роли
    title: Optional[str] = None  # Название роли

class SkbKontur_Talk_Web_Entities_UserRoles_TalkUserRoleUpdateRequest(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Entities.UserRoles.TalkUserRoleUpdateRequest."""
    title: str  # Название роли
    description: Optional[str] = None  # Описание роли
    permissions: List[SkbKontur_Talk_Web_Entities_UserRoles_TalkUserRolePermissionValue]  # Список разрешений роли

class SkbKontur_Talk_Web_Services_TalkUserProfileUpdateResult(BaseModel):
    """Generated model for SkbKontur.Talk.Web.Services.TalkUserProfileUpdateResult."""
    avatarUrl: Optional[str] = None

class SkbKontur_Talk_Whiteboards_Api_Models_TalkWhiteboardsStatistics(BaseModel):
    """Generated model for SkbKontur.Talk.Whiteboards.Api.Models.TalkWhiteboardsStatistics."""
    talkWhiteboardsCount: Optional[int] = None  # Количество досок
